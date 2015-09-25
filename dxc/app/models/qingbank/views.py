#-*- coding:utf-8 -*-

import flaskframe.core
from .models import Contact, Department, DocNode 

class ContactView(flaskframe.core.AuthModelView):
    """Admin view for :class:`~dxc.qingbank.models.Contact`"""

    allowRoles = (u'通讯录管理员',)
    column_searchable_list = ('name', 'name_shot', 'name_pinyin')
    column_exclude_list = ('user',)
    def __init__(self):
        super(ContactView, self).__init__(Contact, flaskframe.core.db.session, name="Contacts", endpoint="contacts", category='Qingbank')

class DepartmentView(flaskframe.core.AuthModelView):
    """Admin view for :class:`~dxc.qingbank.models.Department`"""

    column_searchable_list = ('name',)
    def __init__(self):
        super(DepartmentView, self).__init__(Department, flaskframe.core.db.session, name="Departments", endpoint="departments", category='Qingbank')

class DocNodeView(flaskframe.core.AuthModelView):
    """Admin view for :class:`~dxc.qingbank.models.DocNode`"""
    def __init__(self):
        super(DocNodeView, self).__init__(DocNode, flaskframe.core.db.session, name="DocNodes", endpoint="docnodes", category='Qingbank')
