# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, session, g, current_app, url_for
from flask.ext.security import login_user, LoginForm, current_user
from flask.ext.security.utils import get_url
from werkzeug.local import LocalProxy

from . import route

from sanction import Client
from urlparse import parse_qsl
import re
from json import loads
import urllib

bp = Blueprint('kinorsi-frontend', __name__, template_folder='templates', static_folder='static')
_security = LocalProxy(lambda: current_app.extensions['security'])
_datastore = LocalProxy(lambda: _security.datastore)

def qq_parser(res):
	"""OAuth2 response parser for QQ """
	try:
	    match = re.match('callback\((.*)\)', res)
	    if match != None:
	    	result = match.group(1)
	        jsonRes = loads(result)
	    else:
	        jsonRes = loads(res)
	except ValueError:
	    jsonRes = dict(parse_qsl(res))

	if jsonRes.has_key('expires_in'):
		jsonRes['expires_in'] = long(jsonRes['expires_in'])
	
	return jsonRes	   

@bp.route('/')
def index():
    """Return index page"""
    return render_template('kinorsi/index.html')

@bp.route('/openid/<provider>')
def openid_authenticate(provider):
	"""return openid authenticate url for client to authenticate"""
	oauth_kwargs = current_app.config[str.format('OAUTH_{0}', provider.upper())]
	c = Client(**oauth_kwargs)

	return redirect(c.auth_uri(redirect_uri=str.format('{0}/openid/{1}/login', current_app.config['KINORSI_SERVER_HOST'], provider)))

@bp.route('/openid/<provider>/login')
def openid_login(provider):
	# get parser for provider
	parser = eval(str.format('{0}_parser', provider.lower()))
	code = request.args.get('code')
	oauth_kwargs = current_app.config[str.format('OAUTH_{0}', provider.upper())]
	c = Client(**oauth_kwargs)	
	# get request token
	c.request_token(parser=parser, redirect_uri="kinorsi.com", grant_type='authorization_code', code=code)

	if hasattr(c, 'error') and c.error != 0:
		print 'error:', c.error_description
	else:
		session['access_token'] = c.access_token
		session['refresh_token'] = c.refresh_token
		session[u'expires_in'] = c.expires_in
		# get open id
		res = c.request("/oauth2.0/me", parser=parser)
		res['oauth_consumer_key'] = res['client_id']
		# get nickname. 
		user_info = c.request('/user/get_user_info?' + urllib.urlencode(res), method='GET', parser=parser)

		# 看看是不是已经在数据库中了，没有就写一个
		security = current_app.extensions['security']
		datastore = security.datastore
		user = datastore.find_user(openid=res['openid'], provider=provider.lower())
		if user is None:
			user = datastore.create_user(openid=res['openid'], provider=provider.lower(), nickname=user_info['nickname'])
			datastore.commit()
		else:
			print 'user :', user.username, 'is here'

		login_user(user)

		next_url = get_url(request.args.get('next')) or get_url(request.form.get('next')) or ''
		
		# 如果用户没有绑定，可以让用户尝试进行首次的帐号绑定。如果不绑也可以在以后再绑
		if user.bind_username is None and user.bind_email is None:
			return redirect(url_for('.bind_user'))

		return redirect(next_url)
			
@bp.route('/openid/bind', methods=['GET', 'POST'])
def bind_user():
	"""Bind user local account with openid account"""
	form_class = _security.login_form
	form = form_class()

	if form.validate_on_submit():
		# 这里要确认用户为username还是邮箱
		match = re.match(r'^.+@[^.].*\.[a-z]{2,10}$', form.email.data, re.IGNORECASE)
		if match is None:
			current_user.bind_username = form.email.data
		else:
			current_user.bind_email = form.email.data
			
		_datastore.put(current_user)
		_datastore.commit()

		next_url = get_url(request.args.get('next')) or get_url(request.form.get('next')) or ''
		return redirect(next_url)
		
	return render_template('security/bind_user.html', bind_form=form)
