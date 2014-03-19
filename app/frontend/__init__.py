#-*- coding:utf-8 -*-

from functools import wraps

from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user, login_required

from .. import appfactory
from ..core import admin, db
from ..qingbank.models import Contact, Department, DocNode
from ..security.models import Role, User

# 控制管理面板FLask-Admin的权限
class AuthModelView(ModelView):
    '''Roles that allow to access the view.'''
    allowRoles = ()
    def is_accessible(self):
        return  current_user.has_role('超级管理员') or self._hasOtherRole()
        #return  current_user.is_authenticated() #最好用角色
    def _hasOtherRole(self):
        for r in self.allowRoles:
            if current_user.has_role(r):
                return True
        return False


class UserView(AuthModelView):
    column_searchable_list = ('username',)
    #内联一个表单
    # inline_models = (Contact,)
    column_exclude_list = ('email',)
    def __init__(self):
        super(UserView, self).__init__(User, db.session, name='Users', endpoint='users', category='User Manage')

class RoleView(AuthModelView):
    column_searchable_list = ('name',)
    def __init__(self):
        super(RoleView, self).__init__(Role, db.session, name="Roles", endpoint="roles", category='User Manage')

class ContactView(AuthModelView):
    allowRoles = ('通讯录管理员',)
    column_searchable_list = ('name', 'name_shot', 'name_pinyin')
    column_exclude_list = ('user',)
    def __init__(self):
        super(ContactView, self).__init__(Contact, db.session, name="Contacts", endpoint="contacts", category='Qingbank')

class DepartmentView(AuthModelView):
    column_searchable_list = ('name',)
    def __init__(self):
        super(DepartmentView, self).__init__(Department, db.session, name="Departments", endpoint="departments", category='Qingbank')

class DocNodeView(AuthModelView):
    def __init__(self):
        super(DocNodeView, self).__init__(DocNode, db.session, name="DocNodes", endpoint="docnodes", category='Qingbank')


def create_app(settings_override=None):
    """Different app use this to create app."""
    app = appfactory.create_app(__name__, __path__, settings_override)

    # Init assets
    # assets.init_app(app)

    # init Flask-Admin views
    admin.add_view(UserView())
    admin.add_view(RoleView())
    admin.add_view(ContactView())
    admin.add_view(DepartmentView())
    admin.add_view(DocNodeView())

    admin.init_app(app)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

    return app

def handle_error(e):
    #500的系统错误需要回滚db，不然数据库状态不对
    if e == 500:
        db.session.rollback()
    return render_template('%s.html' % e.code), e.code    

#用于frotend的route
def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator
