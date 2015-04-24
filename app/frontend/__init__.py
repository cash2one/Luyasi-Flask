#-*- coding:utf-8 -*-

from functools import wraps
from collections import namedtuple

from flask import render_template, abort, g, request, session
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user, login_required
from flask_admin import Admin
from flask_principal import Permission

from .. import appfactory
from ..core import db, AuthModelView, RightNeed, babel
from ..qingbank.models import Contact, Department, DocNode
from ..security.models import Role, User
from ..helpers import collect_admin_views, JSONEncoder

def create_app(settings_override=None):
    """Create frontend application.

    :param settings_override: settings that need to override Default to None.
    """
    app = appfactory.create_app(__name__, __path__, settings_override)
    app.json_encoder = JSONEncoder

    #这个只有网页上使用，放在这里的最大原因是为了防止在单元测试时重复增加adminview的endpoint
    admin = Admin(name='Admin', base_template='admin/admin_base.html')
    collect_admin_views(admin)
    admin.init_app(app)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404, 403]:
            app.errorhandler(e)(handle_error)

    init_context_processor(app)

    return app

def handle_error(e):
    """Handler server errors for flask.
    """

    #500的系统错误需要回滚db，不然数据库状态不对
    if e == 500:
        db.session.rollback()
    return render_template('%s.html' % e.code), e.code

#用于frontend的route
def route(bp, *args, **kwargs):
    """Route decorator for frontend application.
    :param bp: original blueprint.
    """

    def decorator(f):
        #@bp.route(*args, **kwargs)
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        #return bp.route(*args, **kwargs)(wrapper)
        # 这样就可以处理多个映射的问题。
        for arg in args:
            wrapper = bp.route(arg, **kwargs)(wrapper)
        return wrapper

    return decorator

#----------------------------------------------------------------------
def right_require(app):
    """用来做RightNeed(action, app, entity)这样的验证的。其中action,entity从方法的名字中取。
    :param app: App name.
    :parma id: Entity id.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*arg, **kwargs):
            action, entity = f.__name__.split('_')
            per = Permission(RightNeed(action, app, entity))
            if not per.can():
                abort(403)
            return f(*arg, **kwargs)

        return wrapper
    return decorator

#----------------------------------------------------------------------
def init_context_processor(app):
    """注册页面用的方法"""
    from ..security.jinjahelpers import has_role_processor, has_right_processor, use_momentjs
    from ..momentjs import momentjs
    from ..frontend.xiaoyuan import is_charger_processor
    # context_processor 是个decorator
    app.context_processor(has_role_processor)
    app.context_processor(has_right_processor)
    app.context_processor(use_momentjs)
    app.context_processor(is_charger_processor)

@babel.localeselector
def get_locale():
    lang = session.get('lang', None)
    if lang is not None:
        return lang
    #m = request.accept_languages.best_match(['zh', 'en'])
    #return m
    return 'zh'

#@babel.timezoneselector
#def get_timezone():
    #user = getattr(g, 'user', None)
    #if user is not None:
        #return user.timezone