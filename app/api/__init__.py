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

    # Register custom error handlers
    if app.debug:
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
    return jsonres(rv=None, metacode=404, msg='Not found')

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


def jsonres(rv=None, metacode=200, msg='', code=200):
    '''这样api可以返回一致的结构。主要是
    '''
#    code = 200
 #   msg = ''
    #if isinstance(res, tuple):
        #rv = res[0]
        #code = res[1]
        #if len(res)==3:
            #msg = res[2]
    return jsonify(dict(response=rv, meta=dict(code=metacode, msg=msg))), code

def paginationInfo(pagination):
    '''返回分布信息用
    @param pagination 分页信息
    '''
    return dict(hasNext=pagination.has_next, hasPrev=pagination.has_prev, nextNum=pagination.next_num,
                            page=pagination.page, pages=pagination.pages, perPage=pagination.per_page, total=pagination.total)    
