# -*- coding: utf-8 -*-
"""
    $(filename)
    ~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

import app.core
from .models import Academy, Class, Message

class AcademyView(app.core.AuthModelView):
    column_list=('name',)
    def __init__(self):
        super(AcademyView, self).__init__(Academy, app.core.db.session, name="Academies", endpoint="academies", category='Xiaoyuan')

class ClassView(app.core.AuthModelView):
    column_list=('name','academy')
    def __init__(self):
        super(ClassView, self).__init__(Class, app.core.db.session, name="Classes", endpoint="classes", category='Xiaoyuan')

class MessageView(app.core.AuthModelView):
    column_list=('content','sender', 'receiver')
    def __init__(self):
        super(MessageView, self).__init__(Message, app.core.db.session, name="Messages", endpoint="messages", category='Xiaoyuan')        