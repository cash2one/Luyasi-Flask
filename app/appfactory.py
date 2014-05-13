# -*- coding:utf-8 -*-

from app import setting
from app.security.models import Role, User
from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore

from .core import db, security, babel, mail
from .helpers import register_blueprints, SslSTMPHandler


def create_app(package_name, package_path, settings_override=None, register_security_blueprint=True):
    """
    Create Flask application. 
    Currently used modules that need to init includes:

    * `Flask-SQLAlchemy <https://pythonhosted.org/Flask-SQLAlchemy>`_
    * `Flask-Mail <http://pythonhosted.org/Flask-Mail/>`_
    * `Flask-Babel <http://pythonhosted.org/Flask-Babel/>`_
    * `Flask-Security <http://pythonhosted.org/Flask-Security/>`_
    * `Flask-Amdin(only init from the frontend) <http://flask-admin.readthedocs.org/en/latest/index.html>`_ 

    :param package_name: package name of the app.
    :param package_path: package path of the app.
    :param settings_override: setting that will override the existed setting items.
    :param register_security_blueprint: flag to specify if the Flask-Security to register blueprint or not.
    """
    app = Flask(package_name, instance_relative_config=True)
    # 基本配置
    app.config.from_object(setting)
    # 可以被覆盖的配置，如在测试情况里
    app.config.from_object(settings_override)

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
        from logging.handlers import RotatingFileHandler, SMTPHandler
        mail_handler = SslSTMPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']), app.config['MAIL_DEFAULT_SENDER'],
                                      app.config['ADMINS'], 'kinoris.com  failed!', credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']))
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.addHandler(mail_handler)

        # 文件log
        import os
        if not os.path.exists(app.config['LOGGING_DIR']):
            os.makedirs(app.config['LOGGING_DIR'])
        file_handler = RotatingFileHandler(os.path.join(app.config['LOGGING_DIR'], 'app.log'), mode='a', maxBytes=5 * 1024 * 1024, backupCount=10, encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        # 默认log
        app.logger.setLevel(logging.INFO)
        app.logger.info(str.format('{0} startup.', app.name))

    return app