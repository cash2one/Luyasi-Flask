#-*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms.fields import TextField, HiddenField, IntegerField, SelectField, TextAreaField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required, Length
from flask_babel import gettext, lazy_gettext

from ..framework.ckeditor import CKEditorField, CKEditorRequired
from ..framework.wtfext.fields import CaptchaField

########################################################################
class BlogForm(Form):
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    title = TextField(lazy_gettext(u'Title'), validators=[Required()])
    category = SelectField(lazy_gettext(u'Blog type'), choices=[#(0, lazy_gettext(u'Blog')), 
                                                                (1, lazy_gettext(u'Xiaoyuan News')), 
                                                                (2, lazy_gettext(u'Life points'))], coerce=int)
    content = CKEditorField(lazy_gettext(u'Content'), import_js=True, validators=[CKEditorRequired(message=gettext('The comment forgot you~'))])
    captcha = CaptchaField()

########################################################################
class CommentForm(Form):
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    #content = CKEditorField(lazy_gettext(u'Comment'), validators=[CKEditorRequired(message=gettext('The comment forgot you~'))])
    content = TextAreaField(lazy_gettext(u'Comment'), validators=[Required()])
    captcha = CaptchaField()


