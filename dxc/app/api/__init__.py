#-*- coding:utf-8 -*-
"""
对外的接口
"""

from functools import wraps

from flask import jsonify
from flask_security import auth_required

from flaskframe import appfactory
from flaskframe.core import db
from flaskframe.helpers import JSONEncoder, check_app_key, jsonres


def create_app(settings_override=None, register_security_blueprint=True):
    app = appfactory.create_app(__name__, __path__, settings_override=settings_override, register_security_blueprint=register_security_blueprint)
    app.json_encoder = JSONEncoder

    # 注册app检测
    # if not app.debug:
    app.before_request(check_app_key)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404, 403]:
            app.errorhandler(e)(handle_error)

    return app

def handle_error(e):
    """Handler server errors for flask.
    """
    #500的系统错误需要回滚db，不然数据库状态不对
    if e == 500:
        db.session.rollback()

    #这个表示内容的是问题的，但是返回正常的协议。
    return jsonres(rv=None, metacode=e.code, msg=str.format("{}: {}", e.name, e.description) , code=e.code)

def route(bp, *args, **kwargs):
    # kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        #@bp.route(*args, **kwargs)
        # @auth_token_required
        @auth_required('session', 'token')
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        #return bp.route(*args, **kwargs)(wrapper)
        # 这样就可以处理多个映射的问题。
        for arg in args:
            wrapper = bp.route(arg, **kwargs)(wrapper)
        return wrapper

    return decorator


# def jsonres(rv=None, metacode=200, msg='', code=200):
#     '''这样api可以返回一致的结构。
#     @param rv 主要的返回内容
#     @param metacode 业务上的代码
#     @param msg 简要信息
#     @param desc 详细描述
#     @param code 这是http返回的statucode
#     '''
# #    code = 200
#  #   msg = ''
#     #if isinstance(res, tuple):
#         #rv = res[0]
#         #code = res[1]
#         #if len(res)==3:
#             #msg = res[2]
#     return jsonify(dict(response=rv, meta=dict(code=metacode, msg=msg))), code

