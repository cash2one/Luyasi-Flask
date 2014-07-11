#-*- coding:utf-8 -*-

from flask_wtf import Form
from flask_babel import lazy_gettext
from wtforms.fields import TextField
from wtforms.validators import Length
from wtforms.ext.sqlalchemy.orm import model_form

from .models import Contact
from ..core import db


class ContactForm(Form):
    name = TextField(lazy_gettext(u'Name'))
    duty = TextField(lazy_gettext(u'Duty'))
    #department = TextField('部门')
    mobile = TextField(lazy_gettext(u'Mobile'))
    telephone =TextField(lazy_gettext(u'Telephone'))
    innerphone = TextField(lazy_gettext(u'Innerphone'))
    fax = TextField(lazy_gettext(u'Fax'))


CF = model_form(Contact,
                db_session=db.session,
                base_class=Form,
                exclude=['user', 'qq', 'name_shot', 'name_pinyin'],
                field_args ={
                    'fax':{
                        'label': lazy_gettext(u'Fax')
                    }, 'name': {
                        'label': lazy_gettext(u'Name')
                    }, 'department':{
                        'label': lazy_gettext(u'Dept')
                    }, 'duty': {
                        'label': lazy_gettext(u'Duty')
                    }, 'mobile': {
                        'label': lazy_gettext(u'Mobile')
                    }, 'telephone': {
                        'label': lazy_gettext(u'Telephone')
                    }, 'innerphone': {
                        'label': lazy_gettext(u'Innerphone')
                    }, 'description': {
                        'label': lazy_gettext(u'Description')
                    }
                })