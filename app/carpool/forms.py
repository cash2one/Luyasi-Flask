# -*- coding: utf-8 -*-
"""
   	Carpool forms.
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime

from flask_wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField, TextAreaField, FloatField, DateTimeField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required, Length
from flask_babel import gettext, lazy_gettext

from ..framework.ckeditor import CKEditorField, CKEditorRequired
from ..framework.wtfext.widgets import DatetimeWidget
from ..framework.wtfext.fields import CaptchaField

########################################################################
class CarpoolForm(Form):
	id = IntegerField(u'id', default=0, widget=HiddenInput())
	start = TextField(lazy_gettext(u'Start point'), validators=[Required()])
	target = TextField(lazy_gettext(u'Target point'), validators=[Required()])
	route = TextAreaField(lazy_gettext(u'Route'))
	price = FloatField(lazy_gettext(u'Price'), validators=[Required()])
	start_time = DateTimeField(lazy_gettext(u'Send out time'), default=datetime.now(), format='%Y-%m-%d %H:%M', widget=DatetimeWidget(), validators=[Required()])
	contact_info = TextAreaField(lazy_gettext(u'Contact info'), validators=[Required()])
	captcha = CaptchaField()