# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField, TextAreaField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required
from flask_babel import gettext, lazy_gettext

from flaskframe.ckeditor import CKEditorField, CKEditorRequired
from flaskframe.wtfext.fields import CaptchaField


########################################################################
class BlogForm(Form):
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    title = TextField(lazy_gettext(u'Title'), validators=[Required()])
    category_id = SelectField(lazy_gettext(u'发表栏目'), choices=[  # (0, lazy_gettext(u'Blog')),
                                                                (1, lazy_gettext(u'Xiaoyuan News')),
                                                                (2, lazy_gettext(u'Life points')),
                                                                (3, u'博客'),
                                                                (4, u'物业公告'),
                                                                (5, u'通知通告'),
                                                                (6, u'有滋有味'),
                                                                (7, u'动弹')],
                              coerce=int, validators=[Required()])
    content = CKEditorField(lazy_gettext(u'Content'), import_js=True,
                            validators=[CKEditorRequired(message=gettext('The comment forgot you~'))])
    captcha = CaptchaField()


########################################################################
class BlogUpdateForm(Form):
    """Used for update"""
    title = TextField(lazy_gettext(u'Title'), validators=[Required()])
    content = CKEditorField(lazy_gettext(u'Content'), import_js=True, validators=[CKEditorRequired(message=u'内容不能为空')])


########################################################################
class CommentForm(Form):
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    # content = CKEditorField(lazy_gettext(u'Comment'), validators=[CKEditorRequired(message=gettext('The comment forgot you~'))])
    content = TextAreaField(lazy_gettext(u'Comment'), validators=[Required()])
    captcha = CaptchaField()
