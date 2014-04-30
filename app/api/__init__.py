#-*- coding:utf-8 -*-
"""
对外的接口
"""

from functools import wraps

from flask import jsonify
from flask.ext.security import (auth_token_required, login_required, SQLAlchemyUserDatastore)

from .. import appfactory
from ..core import db, security
from ..helpers import JSONEncoder


def create_app(settings_override=None, register_security_blueprint=True):
    app = appfactory.create_app(__name__, __path__, settings_override=settings_override, register_security_blueprint=register_security_blueprint)
    app.json_encoder = JSONEncoder

    return app

def route(bp, *args, **kwargs):
    # kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        # @login_required
        @auth_token_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(response=rv, meta=dict(code=sc))), sc
        return f

    return decorator
