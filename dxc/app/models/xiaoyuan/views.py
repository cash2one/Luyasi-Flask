# -*- coding: utf-8 -*-
"""
    $(filename)
    ~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

import flaskframe.core
from .models import Academy, Class, Message, ClassUserAssociation

class AcademyView(flaskframe.core.AuthModelView):
    column_list=('name',)
    def __init__(self):
        super(AcademyView, self).__init__(Academy, flaskframe.core.db.session, name=u"学院", endpoint="academies", category=u'校园管理')

class ClassView(flaskframe.core.AuthModelView):
    column_list=('name','academy')
    def __init__(self):
        super(ClassView, self).__init__(Class, flaskframe.core.db.session, name=u"班级", endpoint="classes", category=u'校园管理')

class MessageView(flaskframe.core.AuthModelView):
    column_list=('content','sender', 'receiver')
    def __init__(self):
        super(MessageView, self).__init__(Message, flaskframe.core.db.session, name=u"消息", endpoint="messages", category=u'校园管理')
        
class ClassUserView(flaskframe.core.AuthModelView):
    def __init__(self):
        super(ClassUserView, self).__init__(ClassUserAssociation, flaskframe.core.db.session, name=u"负责人", endpoint="chagers", category=u'校园管理')