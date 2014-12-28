# -*- coding: utf-8 -*-
"""
    app.security.forms
    ~~~~~~~~~~~
    Other forms that exceed the flask_security.

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime

from flask_wtf import Form
from wtforms.fields import TextField, HiddenField, IntegerField, SelectField, TextAreaField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required, Length
from flask_babel import gettext, lazy_gettext

from ..framework.ckeditor import CKEditorField, CKEditorRequired
from ..framework.wtfext.fields import CaptchaField, DateTimeField, DateField
from ..framework.wtfext.widgets import DatetimeWidget


########################################################################
class ProfileForm(Form):
    """"""
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    nickname = TextField(u'昵称', validators=[Required()])
    sex = SelectField(lazy_gettext(u'性别'), choices=[(0, lazy_gettext(u'女生')),
                                                        (1, lazy_gettext(u'男生')),
                                                        (2, lazy_gettext(u'喜欢女生')),
                                                        (3, lazy_gettext(u'喜欢男生')),
                                                        (100, lazy_gettext(u'保密哦'))], coerce=int)

    truename = TextField(u'真实姓名', validators=[Length(max=10)])
    mobile = TextField(u'手机')
    email = TextField(u'邮箱')
    college = TextField(u'所在学校', validators=[Length(max=30)])
    in_college_date = DateField(lazy_gettext(u'入学时间'), default=None, format='%Y-%m-%d', widget=DatetimeWidget())
    major = TextField(u'专业', validators=[Length(max=30)])
    clazz = TextField(u'所在班级', validators=[Length(max=30)])
    hobby = TextAreaField(u'兴趣爱好', validators=[Length(max=100)])
    special = TextAreaField(u'特长', validators=[Length(max=100)])
    hometown = TextField(u'家乡', validators=[Length(max=100)])
    captcha = CaptchaField()







