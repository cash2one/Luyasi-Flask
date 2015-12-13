# -*- coding: utf-8 -*-
"""
    Jinja template helper. see `http://flask.pocoo.org/docs/templating/#context-processors`_
    ~~~~~~~~~~~

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

from flask_principal import RoleNeed, Permission

from flaskframe.core import RightNeed
from flaskframe.momentjs import momentjs

def has_role_processor():
    """Jinja context processor for role test."""
    def has_role(role):
        # 不加个unicode中文就没得玩了
        role = unicode(role)
        can = Permission(RoleNeed(role)).can()
        return can
    return dict(has_role=has_role)

def has_right_processor():
    """Jinja context processor for right test."""
    def has_right(action, app, entity):
        return Permission(RightNeed(action, app, entity)).can()
    return dict(has_right=has_right)

def use_momentjs():
    """Jinja context processor for use moment js."""
    return dict(momentjs=momentjs)