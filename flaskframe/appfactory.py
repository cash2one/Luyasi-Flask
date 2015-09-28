# -*- coding:utf-8 -*-

from flask import Flask
from flask_security import SQLAlchemyUserDatastore, current_user
from flask_principal import identity_loaded

from flaskframe import setting
from dxc.app.models.security.models import Role, User
from flaskframe.core import db, security, babel, mail, RightNeed, MatrixConverter
from flaskframe.helpers import register_blueprints, SslSTMPHandler


def create_app(package_name, package_path, settings_override=None, register_security_blueprint=True):
    """
    Create Flask application.
    Currently used modules that need to init includes:

    * `Flask-SQLAlchemy <https://pythonhosted.org/Flask-SQLAlchemy>`_
    * `Flask-Mail <http://pythonhosted.org/Flask-Mail/>`_
    * `Flask-Babel <http://pythonhosted.org/Flask-Babel/>`_
    * `Flask-Security <http://pythonhosted.org/Flask-Security/>`_
    * `Flask-Amdin(only init from the frontend) <http://flask-admin.readthedocs.org/en/latest/index.html>`_

    :param package_name: package name of the dxc.
    :param package_path: package path of the dxc.
    :param settings_override: setting that will override the existed setting items.
    :param register_security_blueprint: flag to specify if the Flask-Security to register blueprint or not.
    """
    app = Flask(package_name, instance_relative_config=True)
    # 增加matrix转换器
    app.url_map.converters['matrix'] = MatrixConverter


    # principal
    identity_loaded.connect_via(app)(_app_on_identity_loaded)
    # 公共配置
    app.config.from_object(setting)
    # 可以被覆盖的配置，如在测试情况里
    app.config.from_object(settings_override)
    # 加载security翻译配置
    if app.config.has_key('SECURITY_TRANSLATION_PATH'):
        import importlib
        security_translate = importlib.import_module(app.config['SECURITY_TRANSLATION_PATH'])
        app.config.from_object(security_translate)

    # 使用这样的方式init，不能调用db.create_all()
    db.init_app(app)

    mail.init_app(app)

    # init babel
    babel.init_app(app)

    # init Flask-Security
    security_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, security_datastore, register_blueprint=register_security_blueprint)

    # 注册view
    register_blueprints(app, package_name, package_path)

    # 邮件log
    if not app.debug and not app.testing:
        import logging
        from logging.handlers import RotatingFileHandler
        mail_handler = SslSTMPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']), app.config['MAIL_DEFAULT_SENDER'],
                                      app.config['ADMINS'], 'kinoris.com  failed!', credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']))
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.addHandler(mail_handler)

        # 文件log
        import os
        if not os.path.exists(app.config['LOGGING_DIR']):
            os.makedirs(app.config['LOGGING_DIR'])

        # 一般日志
        file_handler = RotatingFileHandler(os.path.join(app.config['LOGGING_DIR'], 'app.log'), mode='a', maxBytes=5 * 1024 * 1024, backupCount=10, encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        # 错误日志
        file_handler_error = RotatingFileHandler(os.path.join(app.config['LOGGING_DIR'], 'app_error.log'), mode='a', maxBytes=5 * 1024 * 1024, backupCount=10, encoding='utf-8')
        file_handler_error.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)

        # 默认log
        app.logger.setLevel(logging.INFO)
        app.logger.info(str.format('{0} startup.', app.name))

    return app

#----------------------------------------------------------------------
def _app_on_identity_loaded(sender, identity):
    """Define dxc needed flask_pricipal identity loaded handler.
    :param sender: Signle sender.
    "param identity: Identity.
    """
    #identity.provides.add(ItemNeed('delete', 13, 'blog'))
    if current_user.get_id() is not None:
        for right in current_user.rights:
            identity.provides.add(RightNeed(right.action, right.app, right.entity))

        for role in current_user.roles:
            for r in role.rights:
                identity.provides.add(RightNeed(r.action, r.app, r.entity))