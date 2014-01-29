#-*- coding:utf-8 -*-

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = frozenset(['kinorsi@gmail.com'])
# SecretKeyForSessionSigning
SECRET_KEY = 'luyasikinorsi'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'luyasi_flask.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "kinorsiluyasi"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

#: Flask-Security config
SECURITY_TRACKABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
# 登陆时可以选用的字段
SECURITY_USER_IDENTITY_ATTRIBUTES = ['email','username']
#修改密码后不发邮件
SECURITY_SEND_PASSWORD_CHANGE_EMAIL =  False
SECURITY_URL_PREFIX = '/security'
SECURITY_POST_LOGIN_VIEW = '/qingbank/'
SECURITY_POST_LOGOUT_VIEW = '/qingbank/'
SECURITY_MSG_LOGIN = (u'请登陆来后再访问这个页面', 'info')
# 可以注册
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_TOKEN_AUTHENTICATION_HEADER = 'auth_token'
SECURITY_TOKEN_AUTHENTICATION_KEY = 'auth_token'

# babel config
BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'
BABEL_DEFAULT_TIMEZONE = 'UTC'
#related command-working dir: app
# 抽取: pybabel extract -F babel.cfg -o messages.pot .
# 生成：pybabel init -i messages.pot -d frontend/translations -l cs