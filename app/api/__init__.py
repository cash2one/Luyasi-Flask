#-*- coding:utf-8 -*-
"""
对外的接口
"""

from functools import wraps

from flask import jsonify
from flask_security import (auth_token_required, login_required, SQLAlchemyUserDatastore)

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
        @auth_token_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            rv = f(*args, **kwargs)
            return jsonres(rv)
        return f

    return decorator


def jsonres(*res):
    '''这样api可以返回一致的结构。主要是
    '''
    code = 200
    msg = ''
    if isinstance(res, tuple):
        rv = res[0]
        code = res[1]
        if len(res)==3:
            msg = res[2]
    return jsonify(dict(response=rv, meta=dict(code=code, msg=msg))), code

