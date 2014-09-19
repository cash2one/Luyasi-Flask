# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField, TextAreaField, FieldList, FileField, SelectMultipleField, HiddenField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required
from flask_babelex import lazy_gettext

from ..framework.wtfext.fields import Select2Field

class MsgForm(Form):
    receivers = Select2Field(lazy_gettext(u'Receivers'))
    content = TextAreaField(lazy_gettext(u'Content'), validators=[Required()])
    #attach = FieldList(FileField(), min_entries=2)
    attach = FileField(lazy_gettext(u'Attach'))

class ReplayForm(Form):
    content = TextAreaField (lazy_gettext(u'Content'), validators=[Required()])
    attach = FileField(lazy_gettext(u'Attach'))