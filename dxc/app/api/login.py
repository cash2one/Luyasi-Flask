#-*- coding:utf-8 -*-

from . import route

from flask import Blueprint, url_for, current_app, request
import requests
import re
import json

from . import jsonres

bp = Blueprint('api_login', __name__)


@bp.route('/login', methods=['POST'])
def login():
    """"""

    username = request.json.get('username', '')
    passwd = request.json.get('password', '')

    # print username

    loginUrl = url_for('security.login')
    loginUrl = current_app.config['API_URL'] + loginUrl

    res = requests.get(loginUrl)

    # print 'cookies:', res.headers['set-cookie']
    content = res.text
    cookies = res.cookies #Must send back the cookies, or the server can't make correct crsf_token

    pattern = '<input id="csrf_token" name="csrf_token" type="hidden" value="([\w\.#]+)">'

    match = re.search(pattern, content)
    csrf_token = match.group(1)
    # print 'csrf_token:', csrf_token

    data = {'csrf_token':csrf_token,'email':username, 'password': passwd}
    jdata = json.dumps(data)
    loginRes = requests.post(loginUrl, json=data, cookies=cookies)
    return loginRes.text
    #print loginRes

    # return jsonres(rv=dict(msg='ok'))


@route(bp, '/testlogin', methods=['GET'])
def testlogin():
    return 'ok'