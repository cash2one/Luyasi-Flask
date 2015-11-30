#-*- coding:utf-8 -*-

# 这里不直接引入AuthModeView，而是这么麻烦是为了不在helper.collect_amdin_views里不会引用到AuthModeView
import flaskframe.core
from .models import User, Role, App, Right

class UserView(flaskframe.core.AuthModelView):
    """Admin view for :class:`~dxc.security.models.User`"""

    column_searchable_list = ('username',)
    #内联一个表单
    # inline_models = (Contact,)
    column_exclude_list = ('password','version')
    def __init__(self):
        super(UserView, self).__init__(User, flaskframe.core.db.session, name=u'用户', endpoint='users', category=u'用户管理')

class RoleView(flaskframe.core.AuthModelView):
    """Admin view for :class:`~dxc.security.models.Role`"""

    column_searchable_list = ('name',)
    def __init__(self):
        super(RoleView, self).__init__(Role, flaskframe.core.db.session, name=u'角色', endpoint='roles', category=u'用户管理')

class RightView(flaskframe.core.AuthModelView):
    """Admin view for :class:`~dxc.security.models.Right`"""
    # column_searchable_list = ('dxc',)
    #----------------------------------------------------------------------
    def __init__(self):
        super(RightView, self).__init__(Right, flaskframe.core.db.session, name=u'权限', endpoint='rights', category=u'用户管理')

class AppView(flaskframe.core.AuthModelView):
    """Admin view for :class:`~dxc.security.models.App`"""
    column_searchable_list = ('name','app_version')

    #----------------------------------------------------------------------
    def __init__(self):
        super(AppView, self).__init__(App, flaskframe.core.db.session, name=u'应用', endpoint='apps', category=u'用户管理')

