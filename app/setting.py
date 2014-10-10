#-*- coding:utf-8 -*-

"""
Flask app setting.
"""

import os
from flask.ext.babel import gettext, lazy_gettext

#Flask的debug开关。有利于看出错信息。正式启用时要关掉
DEBUG = True
TESTING = False

#是否需要显示所有的blueprint route
DEBUG_PRINT_ROUTE = False
#: In some case, email will not used at all. e.g. When use qingbank module only.
ENABLE_SECURITY_MAIL = True

# 最大的楼层深度，超过了则会隐藏
BLOG_VISIBLE_MAX_FLOOR = 5

# 验证码设置
RECAPTCHA_PUBLIC_KEY = "6Lex_PQSAAAAAM43C35O-SMHkI6R97koCagyxbNO"
RECAPTCHA_PRIVATE_KEY = "6Lex_PQSAAAAANICoSeoV0BWR_IN3FlBFAawQXHN"

#------基本路径-----------------
_basedir = os.path.abspath(os.path.dirname(__file__))

#---------------------上传配置-----------------------------------------
UPLOAD_FOLDER = os.path.join(_basedir, 'frontend/static/upload')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# 16M upload
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

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
KINORSI_SERVER_HOST = ''
if KINORSI_SERVER_PORT and len(KINORSI_SERVER_PORT)>0:
	KINORSI_SERVER_HOST = str.format('{}:{}', KINORSI_SERVER_NAME, KINORSI_SERVER_PORT)
else:
	KINORSI_SERVER_HOST = KINORSI_SERVER_NAME

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
SECRET_KEY = '\xe2\x95\x96\xd8\xba\xda\xb6\x1e\xf9Ev\n\xfd\x0c\xb6\xca\xf1a9l-S\xe3\xd9'

#和app同一级路径存储log
LOGGING_DIR = os.path.join(_basedir, '../logs')

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'luyasi_flask.db')

# 用mysql的话，alembic的detected有点问题.喜欢重新删除约束，重建，或者修改boolean为tinyint等。。~看来要手动改改代码。我顶他个肺肺
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:qingbank@127.0.0.1/luyasi-flask?charset=utf8&use_unicode=0'
# 模型返回json时最大的解析层次。
SQLALCHMY_MAX_DEPTH = 3
# database migrate
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "kinorsiluyasi"

# Flask-Security 配置
SECURITY_EMAIL_SENDER=MAIL_DEFAULT_SENDER
SECURITY_TRACKABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_REGISTERABLE = True
#加密算法
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'ihvgh08t8h4nbg0a0h'

# 登陆时可以使用的字段
SECURITY_USER_IDENTITY_ATTRIBUTES = ['email','username']

SECURITY_URL_PREFIX = '/security'
# 自己增加的用于openid
SECURITY_OPENID_LOGIN_URL = '/openid_login'
SECURITY_POST_LOGIN_VIEW = '/qingbank/'
SECURITY_POST_LOGOUT_VIEW = '/qingbank/'
SECURITY_POST_REGISTER_VIEW = '/security/register'
SECURITY_POST_CONFIRM_VIEW = '/qingbank/'
SECURITY_POST_CHANGE_VIEW = '/security/change'

#这里似乎做不了本地化，会出现json错误。先不做。
#SECURITY_MSG_LOGIN = (u'请先登陆', 'info')

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
#MOMENTJS_LOCAL = 'zh-cn'
MOMENTJS_LOCAL = 'en'
BABEL_DEFAULT_LOCALE = 'en'
#BABEL_DEFAULT_LOCALE = 'zh'
BABEL_DEFAULT_TIMEZONE = 'UTC'
#related command-working dir: app
# 抽取: pybabel extract -F babel.cfg -o messages.pot .
# 生成：pybabel init -i messages.pot -d frontend/translations -l cs
# 由于security的一些文本有特殊标签如%(value)s，所以需要自己导入。这个会在factory里导入。但是这个一旦启动就不会再理会别外一个语言。后续再处理吧。
if BABEL_DEFAULT_LOCALE != 'en':
	SECURITY_TRANSLATION_PATH='app.security.translations.' + BABEL_DEFAULT_LOCALE
