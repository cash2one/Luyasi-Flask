#-*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms.fields import TextField, HiddenField, IntegerField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required, Length
from flask_babel import gettext, lazy_gettext

from ..framework.ckeditor import CKEditorField, CKEditorRequired
from ..framework.wtfext.fields import CaptchaField

########################################################################
class BlogForm(Form):
	id = IntegerField(u'id', default=0, widget=HiddenInput())
	title = TextField(lazy_gettext(u'Title'), validators=[Required()])
	content = CKEditorField(lazy_gettext(u'Content'), import_js=True, validators=[CKEditorRequired(message=gettext('The comment forgot you~'))])
	captcha = CaptchaField()

########################################################################
class CommentForm(Form):
	id = IntegerField(u'id', default=0, widget=HiddenInput())
	content = CKEditorField(lazy_gettext(u'Comment'), validators=[CKEditorRequired(message=gettext('The comment forgot you~'))])
	captcha = CaptchaField()



