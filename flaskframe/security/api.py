# -*- coding:utf-8 -*-

import re
import json

from flask import Blueprint, url_for, current_app, request, make_response
from flask_security import login_user
from flask_security.utils import verify_and_update_password
from flaskframe.helpers import generate_csrf_token
import requests

from dxc.services import api_user
from ..helpers import jsonres

bp = Blueprint('framework_api_login', __name__)


@bp.route('/login', methods=['POST'])
def login():
    """这里自己调用security的login。主要是为了返回csrfToken给前端的ng使用"""

    email = request.json.get('email', '')
    passwd = request.json.get('password', '')
    app_id = request.headers.get('app_id') or request.args.get('app_id')
    headers = {'app-id': app_id}
    # print username

    loginUrl = url_for(current_app.config['SECURITY_BLUEPRINT_NAME'] + '.login')
    loginUrl = current_app.config['API_URL'] + loginUrl

    data = {'email': email, 'password': passwd}
    jdata = json.dumps(data)
    loginRes = requests.post(loginUrl, json=data, headers=headers)
    resJson = loginRes.json()

    if resJson['meta']['code'] == 200:
        user = api_user.get(int(resJson['response']['user']['id']))
        del resJson['response']['user']['id']
        resJson['response']['user']['nickname'] = user.nickname or user.email
        resJson['meta']['success'] = True
        gen_csrf = generate_csrf_token(user)

    response = make_response(json.dumps(resJson))

    if resJson['meta']['code'] == 200:
        response.set_cookie('XSRF-TOKEN', gen_csrf)

    return response
    # return jsonString


@bp.route('/login2', methods=['POST'])
def login2():
    """这是从内部请求面页的方式做的，比较麻烦。主要是原来想去掉crsf_token"""

    username = request.json.get('username', '')
    passwd = request.json.get('password', '')

    # print username

    loginUrl = url_for('security.login')
    loginUrl = current_app.config['API_URL'] + loginUrl

    res = requests.get(loginUrl)

    # print 'cookies:', res.headers['set-cookie']
    content = res.text
    cookies = res.cookies  # Must send back the cookies, or the server can't make correct crsf_token

    pattern = '<input id="csrf_token" name="csrf_token" type="hidden" value="([\w\.#]+)">'

    match = re.search(pattern, content)
    csrf_token = match.group(1)
    # print 'csrf_token:', csrf_token

    data = {'csrf_token': csrf_token, 'email': username, 'password': passwd}
    jdata = json.dumps(data)
    loginRes = requests.post(loginUrl, json=data, cookies=cookies)
    resJson = loginRes.json()

    if resJson['meta']['code'] == 200:
        user = api_user.get(int(resJson['response']['user']['id']))
        del resJson['response']['user']['id']
        resJson['response']['user']['nickname'] = user.nickname or user.email

    return json.dumps(resJson)


@bp.route('/login3', methods=['POST'])
def login3():
    """直接使用flask-security的工具方法完成登陆验证"""
    username = request.json.get('username', '')
    passwd = request.json.get('password', '')

    security = current_app.extensions['security']
    datastore = security.datastore
    user = datastore.get_user(username)
    if not verify_and_update_password(passwd, user):
        return jsonres(metacode=401, msg=u'用户不在在或密码不正确')

    login_user(user)

    loginRes = dict(authentication_token=user.get_auth_token(), nickname=(user.nickname or user.email),
                    avatar=user.avatar)
    return jsonres(rv=dict(user=loginRes))


@bp.route('/openid/qq/applogin', methods=['POST'])
def app_login():
    """这是app端登陆的方法。app端发送取得的token，这里再取到用户信息进去注册或者登陆"""
    access_token = request.json.get('access_token')
    #openid
    userid = request.json.get('userid')
    appkey = request.json.get('appId');
    # appkey = current_app.config['APPKEY_QQ_MOBILE']
    userInfoUrl = str.format(
        'https://graph.qq.com/user/get_user_info?oauth_consumer_key={0}&access_token={1}&openid={2}&format=json',
        appkey, access_token, userid)
    print userInfoUrl
    res = requests.get(str.format(
        'https://graph.qq.com/user/get_user_info?oauth_consumer_key={0}&access_token={1}&openid={2}&format=json',
        appkey, access_token, userid))

    resJson = res.json()
    if resJson['ret'] != 0:
        return jsonres(rv=resJson)

    userinfo = resJson

    security = current_app.extensions['security']
    datastore = security.datastore
    user = datastore.find_user(openid=userid, provider='qq')
    if user is None:
        user = datastore.create_user(openid=userid, provider='qq', nickname=userinfo['nickname'],
                                     avatar=userinfo['figureurl_qq_1'], bind_remind=0)
        datastore.commit()
    else:
        # 这里把user的openid当成password了~其实这个passwd谁也不知道~只是后面用业生成token时，如果password为空，security里生成token会报错
        if user.password is None:
            user.password = userid
            datastore.commit()
        pass
        # print 'user :', user.username, 'is here'

    login_user(user)

    # print user.get_auth_token()
    loginRes = dict(authentication_token=user.get_auth_token(), nickname=(user.nickname or user.email),
                    avatar=user.avatar)
    return jsonres(rv=dict(user=loginRes))
