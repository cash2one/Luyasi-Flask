#-*- coding:utf-8 -*-
import os

from flask import Blueprint, render_template, send_from_directory, current_app, url_for, abort

from . import route
from ..services import api_job, api_carpool, api_blog

bp = Blueprint('frontend-index', __name__, template_folder='templates', static_folder='static')

#----------------------------------------------------------------------
@bp.route('/')
@bp.route('/<html>')
def index(html=None):
	""""""
	if current_app.debug and html is not None:
		if html=='favicon.ico':
			return send_from_directory(os.path.join(current_app.root_path, 'templates'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
		else:
			pos = html.find('.')
			if pos != -1 :
				return render_template('/%s' % html)
			else:
				abort(404)

	jobs = api_job.get_lastest_page(1, per_page=5)
	carinfos = api_carpool.get_lastest_page(1, per_page=5)
	#blogs = api_blog.get_lastest_page(1, per_page=5)
	return render_template('index/index.html', jobs=jobs, carinfos=carinfos)#, blogs=blogs)

