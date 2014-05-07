#-*- coding:utf-8 -*-

"""
Flask app setting.
"""

import os

#Flask的debug开关。有利于看出错信息。
DEBUG = True

#是否需要显示所有的blueprint route
DEBUG_ROUTE = False

from flask.ext.babel import gettext, ngettext

#OAuth client配置信息
OAUTH_QQ = {
	"auth_endpoint": "https://graph.qq.com/oauth2.0/authorize",	
	"token_endpoint": "https://graph.qq.com/oauth2.0/token",
	"resource_endpoint": "https://graph.qq.com",
	"client_id" :"101055610",
	"client_secret": "15053e08bfb35e21e14a23186457ece6"			
}

#SERVER_NAME就flask的自有配置。。上次不小心用了SERVER_NAME，搞到所有请求都是not found
KINORSI_SERVER_NAME = 'kinorsi.com'
KINORSI_SERVER_PORT = '5000'
KINORSI_SERVER_HOST = str.format('%s:%s', KINORSI_SERVER_NAME, KINORSI_SERVER_PORT)

#: In some case, email will not used at all. e.g. When use qingbank module only.
ENABLE_SECURITY_MAIL = True

#gmail.com-for logging.写log和正常发邮件有所不同。。
# MAIL_DEFAULT_SENDER = "kinorsi@gmail.com"
# MAIL_SERVER = 'smtp.gmail.com'
# MAIL_PORT = 587#465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True
# MAIL_USERNAME = 'kinorsi@gmail.com'
# MAIL_PASSWORD = 'www.gmail.com'

#kinorsi.com - 可用
# MAIL_DEFAULT_SENDER = "postmaster@kinorsi.com"
# MAIL_SERVER = 'smtp.kinorsi.com'
# MAIL_USERNAME = 'postmaster@kinorsi.com'
# MAIL_PASSWORD = 'laogong2LAOPO'

#mail.qq.com-使用helpers.SslSMTPHandler就可以了。
MAIL_DEFAULT_SENDER = "kinorsi@qq.com"
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'kinorsi@qq.com'
MAIL_PASSWORD = 'chouchou2TOUTOU'

#收邮件用的管理员
ADMINS=['172440249@qq.com']


# SecretKeyForSessionSigning
SECRET_KEY = 'luyasikinorsi'

_basedir = os.path.abspath(os.path.dirname(__file__))

#和app同一级路径存储log
LOGGING_DIR = os.path.join(_basedir, '../logs')

#openid dir
# OPENID_FS_STORE_PATH = os.path.join(_basedir, 'openid_tmp')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'luyasi_flask.db')

# database migrate 
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "kinorsiluyasi"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

# Flask-Security 配置
SECURITY_EMAIL_SENDER=MAIL_DEFAULT_SENDER
SECURITY_TRACKABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_REGISTERABLE = True
#加密算法
# SECURITY_PASSWORD_HASH = 'sha512_crypt'
# SECURITY_PASSWORD_SALT = '567HNtH731dfASd45hhHIJHIH'

# 登陆时可以使用的字段
SECURITY_USER_IDENTITY_ATTRIBUTES = ['email','username']
#OpenID的提供方
# OPENID_PROVIDERS = [
#     { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
#     { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#     { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#     { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#     { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

SECURITY_URL_PREFIX = '/security'
# 自己增加的用于openid
SECURITY_OPENID_LOGIN_URL = '/openid_login'
SECURITY_POST_LOGIN_VIEW = '/qingbank/'
SECURITY_POST_LOGOUT_VIEW = '/qingbank/'
SECURITY_POST_REGISTER_VIEW = '/qingbank/'
SECURITY_POST_CONFIRM_VIEW = '/qingbank/'

SECURITY_MSG_LOGIN = (u'请先登陆', 'info')

# 邮件功能
SECURITY_SEND_REGISTER_EMAIL=ENABLE_SECURITY_MAIL #发送注册邮件
SECURITY_SEND_PASSWORD_CHANGE_EMAIL=ENABLE_SECURITY_MAIL #发送密码更新邮件

SECURITY_TOKEN_AUTHENTICATION_HEADER = 'auth_token'
SECURITY_TOKEN_AUTHENTICATION_KEY = 'auth_token'
#注册邮件是否需要进行验证
SECURITY_CONFIRMABLE=ENABLE_SECURITY_MAIL

#flask-security各类邮件头
SECURITY_EMAIL_SUBJECT_REGISTER='感谢您注册kinorsi.com通行证'
SECURITY_EMAIL_SUBJECT_PASSWORDLESS='你使用了kinorsi.com无密码登陆方式'
SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE='您的kinorsi.com通行证已经成功重置'
SECURITY_EMAIL_SUBJECT_PASSWORD_RESET='请验证您的kinorsi.com通行证密码重置'
SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE='您的kinorsi.com通行证密码修改成功'
SECURITY_EMAIL_SUBJECT_CONFIRM='请验证kinorsi.com注册'


# babel config
BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'
BABEL_DEFAULT_TIMEZONE = 'UTC'
#related command-working dir: app
# 抽取: pybabel extract -F babel.cfg -o messages.pot .
# 生成：pybabel init -i messages.pot -d frontend/translations -l cs


#Security 信息翻译用
# SECURITY_MSG_UNAUTHORIZED= (gettext('You do not have permission to view this resource.'), 'error'),
# SECURITY_MSG_CONFIRM_REGISTRATION= (gettext('Thank you. Confirmation instructions have been sent to %(email)s.'), 'success'),
# SECURITY_MSG_EMAIL_CONFIRMED= (gettext('Thank you. Your email has been confirmed.'), 'success'),
# SECURITY_MSG_ALREADY_CONFIRMED= (gettext('Your email has already been confirmed.'), 'info'),
# SECURITY_MSG_INVALID_CONFIRMATION_TOKEN= (gettext('Invalid confirmation token.'), 'error'),
# SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED= (gettext('%(email)s is already associated with an account.'), 'error'),
# SECURITY_MSG_PASSWORD_MISMATCH= (gettext('Password does not match'), 'error'),
# SECURITY_MSG_RETYPE_PASSWORD_MISMATCH= (gettext('Passwords do not match'), 'error'),
# SECURITY_MSG_INVALID_REDIRECT= (gettext('Redirections outside the domain are forbidden'), 'error'),
# SECURITY_MSG_PASSWORD_RESET_REQUEST= (gettext('Instructions to reset your password have been sent to %(email)s.'), 'info'),
# SECURITY_MSG_PASSWORD_RESET_EXPIRED= (gettext('You did not reset your password within %(within)s. New instructions have been sent to %(email)s.'), 'error'),
# SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN= (gettext('Invalid reset password token.'), 'error'),
# SECURITY_MSG_CONFIRMATION_REQUIRED= (gettext('Email requires confirmation.'), 'error'),
# SECURITY_MSG_CONFIRMATION_REQUEST= (gettext('Confirmation instructions have been sent to %(email)s.'), 'info'),
# SECURITY_MSG_CONFIRMATION_EXPIRED= (gettext('You did not confirm your email within %(within)s. New instructions to confirm your email have been sent to %(email)s.'), 'error'),
# SECURITY_MSG_LOGIN_EXPIRED= (gettext('You did not login within %(within)s. New instructions to login have been sent to %(email)s.'), 'error'),
# SECURITY_MSG_LOGIN_EMAIL_SENT= (gettext('Instructions to login have been sent to %(email)s.'), 'success'),
# SECURITY_MSG_INVALID_LOGIN_TOKEN= (gettext('Invalid login token.'), 'error'),
# SECURITY_MSG_DISABLED_ACCOUNT= (gettext('Account is disabled.'), 'error'),
# SECURITY_MSG_EMAIL_NOT_PROVIDED= (gettext('Email not provided'), 'error'),
# SECURITY_MSG_INVALID_EMAIL_ADDRESS= (gettext('Invalid email address'), 'error'),
# SECURITY_MSG_PASSWORD_NOT_PROVIDED= (gettext('Password not provided'), 'error'),
# SECURITY_MSG_PASSWORD_NOT_SET= (gettext('No password is set for this user'), 'error'),
# SECURITY_MSG_PASSWORD_INVALID_LENGTH= (gettext('Password must be at least 6 characters'), 'error'),
# SECURITY_MSG_USER_DOES_NOT_EXIST= (gettext('Specified user does not exist'), 'error'),
# SECURITY_MSG_INVALID_PASSWORD= (gettext('Invalid password'), 'error'),
# SECURITY_MSG_PASSWORDLESS_LOGIN_SUCCESSFUL= (gettext('You have successfuly logged in.'), 'success'),
# SECURITY_MSG_PASSWORD_RESE= (gettext('You successfully reset your password and you have been logged in automatically.'), 'success'),
# SECURITY_MSG_PASSWORD_IS_THE_SAME= (gettext('Your new password must be different than your previous password.'), 'error'),
# SECURITY_MSG_PASSWORD_CHANGE= (gettext('You successfully changed your password.'), 'success'),
# SECURITY_MSG_LOGIN= (gettext('Please log in to access this page.'), 'info'),
# SECURITY_MSG_REFRESH= (gettext('Please reauthenticate to access this page.'), 'info'),