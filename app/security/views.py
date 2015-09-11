#-*- coding:utf-8 -*-

# 这里不直接引入AuthModeView，而是这么麻烦是为了不在helper.collect_amdin_views里不会引用到AuthModeView
import app.core
from .models import User, Role, App, Right

class UserView(app.core.AuthModelView):
    """Admin view for :class:`~app.security.models.User`"""

    column_searchable_list = ('username',)
    #内联一个表单
    # inline_models = (Contact,)
    column_exclude_list = ('password','version')
    def __init__(self):
        super(UserView, self).__init__(User, app.core.db.session, name='Users', endpoint='users', category='Security Manage')

class RoleView(app.core.AuthModelView):
    """Admin view for :class:`~app.security.models.Role`"""

    column_searchable_list = ('name',)
    def __init__(self):
        super(RoleView, self).__init__(Role, app.core.db.session, name="Roles", endpoint="roles", category='Security Manage')

class RightView(app.core.AuthModelView):
    """Admin view for :class:`~app.security.models.Right`"""
    column_searchable_list = ('app',)
    #----------------------------------------------------------------------
    def __init__(self):
        super(RightView, self).__init__(Right, app.core.db.session, name="Rights", endpoint="rights", category='Security Manage')

class AppView(app.core.AuthModelView):
    """Admin view for :class:`~app.security.models.App`"""
    column_searchable_list = ('name','app_version')

    #----------------------------------------------------------------------
    def __init__(self):
        super(AppView, self).__init__(App, app.core.db.session, name="Apps", endpoint="apps", category='Security Manage')

