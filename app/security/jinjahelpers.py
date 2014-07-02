#-*- coding:utf-8 -*-

from flask_principal import RoleNeed, Permission

from ..core import RightNeed

def has_role_processor():
	"""Jinja context processor for role test."""
	def has_role(role):
		can = Permission(RoleNeed(role)).can()
		return can
	return dict(has_role=has_role)

def has_right_processor():
	"""Jinja context processor for right test."""
	def has_right(action, app, entity):
		return Permission(RightNeed(action, app, entity)).can()
	return dict(has_right=has_right)
