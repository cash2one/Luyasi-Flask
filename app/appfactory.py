#-*- coding:utf-8 -*-

from app import config
from app.security.models import Role, User
from flask import Blueprint, Flask, render_template, template_rendered, current_app
from flask.ext.security import SQLAlchemyUserDatastore

from .core import db, security, babel, mail
from .helpers import register_blueprints

def create_app(package_name, package_path, settings_override=None, register_security_blueprint=True):
	"""
	Create Flask application
	"""
	app = Flask(package_name, instance_relative_config=True)
	# app.config.from_object(settings_override)
	app.config.from_object(config)
	# 使用这样的方式init，不能调用db.create_all()
	db.init_app(app)
	mail.init_app(app)

	# init babel
	babel.init_app(app)
	# init Flask-Security
	security_datastore = SQLAlchemyUserDatastore(db, User, Role)
	security.init_app(app, security_datastore)
	
	register_blueprints(app, package_name, package_path)
	
	return app
