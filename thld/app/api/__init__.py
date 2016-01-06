# -*- coding:utf-8 -*-
"""
对外的接口
"""

from functools import wraps

from flask_security import (auth_token_required)

from flaskframe import appfactory
from flaskframe.core import db
from flaskframe.helpers import JSONEncoder, check_app_key, jsonres


def create_app(settings_override=None, register_security_blueprint=True):
    app = appfactory.create_app(__name__, __path__, settings_override=settings_override,
                                register_security_blueprint=register_security_blueprint)
    app.json_encoder = JSONEncoder

    # 注册app检测
    app.before_request(check_app_key)

    # Register custom error handlers
    if app.debug:
        for e in [500, 404, 403]:
            app.errorhandler(e)(handle_error)

    return app


def handle_error(e):
    """Handler server errors for flask.
    """
    # 500的系统错误需要回滚db，不然数据库状态不对
    if e == 500:
        db.session.rollback()

    # 这个表示内容的是问题的，但是返回正常的协议。
    return jsonres(rv=None, metacode=e.code, msg=str.format("{}: {}", e.name, e.description), code=e.code)


def route(bp, *args, **kwargs):
    # kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        # @bp.route(*args, **kwargs)
        @auth_token_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        # return bp.route(*args, **kwargs)(wrapper)
        # 这样就可以处理多个映射的问题。
        for arg in args:
            wrapper = bp.route(arg, **kwargs)(wrapper)
        return wrapper

    return decorator


def paginationInfo(pagination):
    '''返回分布信息用
    @param pagination 分页信息
    '''
    return dict(hasNext=pagination.has_next, hasPrev=pagination.has_prev, nextNum=pagination.next_num,
                page=pagination.page, pages=pagination.pages, perPage=pagination.per_page, total=pagination.total)
