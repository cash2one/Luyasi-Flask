#-*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms.fields import TextField, HiddenField, IntegerField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required, Length
from flask_babel import gettext

from ..framework.ckeditor import CKEditorField, CKEditorRequired
from ..framework.wtfext.fields import CaptchaField

########################################################################
class BlogForm(Form):
	id = IntegerField(u'id', default=0, widget=HiddenInput())
	title = TextField(u'题目', validators=[Required()])
	content = CKEditorField(u'内容', import_js=True, validators=[CKEditorRequired(message=gettext('The comment forgot you~'))])
	captcha = CaptchaField()

########################################################################
class CommentForm(Form):
	id = IntegerField(u'id', default=0, widget=HiddenInput())
	content = CKEditorField(u'评论', validators=[CKEditorRequired(message=gettext('The comment forgot you~'))])
	captcha = CaptchaField()



