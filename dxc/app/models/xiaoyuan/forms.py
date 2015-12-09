# -*- coding: utf-8 -*-
from flask.ext.babel import lazy_gettext
from flask.ext.wtf import Form

from flask_wtf import Form
from wtforms import IntegerField, TextField, SelectField, TextAreaField
from wtforms.fields import TextField, IntegerField, TextAreaField, FileField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required, Length
from flask_babelex import lazy_gettext, gettext

from flaskframe.wtfext.fields import Select2Field, CaptchaField, DateField
from flaskframe.ckeditor import CKEditorField, CKEditorRequired
from flaskframe.wtfext.widgets import DatetimeWidget


class MsgForm(Form):
    receivers = Select2Field(lazy_gettext(u'Receivers'))
    content = TextAreaField(lazy_gettext(u'Content'), validators=[Required()])
    #attach = FieldList(FileField(), min_entries=2)
    attach = FileField(lazy_gettext(u'Attach'))

class ReplayForm(Form):
    content = TextAreaField (lazy_gettext(u'Content'), validators=[Required()])
    attach = FileField(lazy_gettext(u'Attach'))

class MemberInfoForm(Form):
    id = IntegerField(lazy_gettext(u'id'), default=0, widget=HiddenInput())
    name = TextField(lazy_gettext(u'Name'), validators=[Required()])
    student_no = TextField(lazy_gettext(u'Studentno'), validators=[Required()])
    idcard = TextField(lazy_gettext(u'IDcard'), validators=[Required(), Length(min=18, max=18)])
    captcha = CaptchaField()    
    
class NoticeForm(Form):
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    title = TextField(lazy_gettext(u'标题'), validators=[Required()])
    content = CKEditorField(lazy_gettext(u'通知内容'), import_js=True, validators=[CKEditorRequired(message=gettext(u'请填写内容'))])
    captcha = CaptchaField()


class ProfileForm(Form):
    """"""
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    nickname = TextField(u'昵称(填写后不能修改)', validators=[Required(), Length(max=10)])
    sex = SelectField(lazy_gettext(u'性别'), choices=[(0, lazy_gettext(u'女生')),
                                                        (1, lazy_gettext(u'男生')),
                                                        (2, lazy_gettext(u'喜欢女生')),
                                                        (3, lazy_gettext(u'喜欢男生')),
                                                        (100, lazy_gettext(u'保密哦'))], coerce=int)

    truename = TextField(u'真实姓名(填写后不能修改)', validators=[Length(max=10)])
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



