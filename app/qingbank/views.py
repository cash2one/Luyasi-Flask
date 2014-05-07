#-*- coding:utf-8 -*-

import app.core
from .models import Contact, Department, DocNode 

class ContactView(app.core.AuthModelView):
    """Admin view for :class:`~app.qingbank.models.Contact`"""

    allowRoles = (u'通讯录管理员',)
    column_searchable_list = ('name', 'name_shot', 'name_pinyin')
    column_exclude_list = ('user',)
    def __init__(self):
        super(ContactView, self).__init__(Contact, app.core.db.session, name="Contacts", endpoint="contacts", category='Qingbank')

class DepartmentView(app.core.AuthModelView):
    """Admin view for :class:`~app.qingbank.models.Department`"""

    column_searchable_list = ('name',)
    def __init__(self):
        super(DepartmentView, self).__init__(Department, app.core.db.session, name="Departments", endpoint="departments", category='Qingbank')

class DocNodeView(app.core.AuthModelView):
    """Admin view for :class:`~app.qingbank.models.DocNode`"""    
    def __init__(self):
        super(DocNodeView, self).__init__(DocNode, app.core.db.session, name="DocNodes", endpoint="docnodes", category='Qingbank')
