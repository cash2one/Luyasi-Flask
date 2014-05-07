#-*- coding:utf-8 -*-

from functools import wraps

from flask import render_template
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user, login_required
from flask.ext.admin import Admin

from .. import appfactory
from ..core import db, AuthModelView
from ..qingbank.models import Contact, Department, DocNode
from ..security.models import Role, User
from ..helpers import collect_admin_views

def create_app(settings_override=None):
    """Create frontend application.

    :param settings_override: settings that need to override Default to None.
    """
    app = appfactory.create_app(__name__, __path__, settings_override)

    #这个只有网页上使用，放在这里的最大原因是为了防止在单元测试时重复增加adminview的endpoint
    admin = Admin(name='Admin', base_template='admin/admin_base.html')
    collect_admin_views(admin)
    admin.init_app(app)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

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
        @bp.route(*args, **kwargs)
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator
