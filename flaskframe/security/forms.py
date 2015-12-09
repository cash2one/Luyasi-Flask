# -*- coding: utf-8 -*-
"""
    dxc.security.forms
    ~~~~~~~~~~~
    Other forms that exceed the flask_security.

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

from flask_wtf import Form
from wtforms.fields import TextField, IntegerField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required

from flaskframe.wtfext.fields import CaptchaField


########################################################################
class SysMessageForm(Form):
    """"""
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    content = TextField(u'理由', validators=[Required()])
    captcha = CaptchaField()
