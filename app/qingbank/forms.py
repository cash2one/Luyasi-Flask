#-*- coding:utf-8 -*-

from flask_wtf import Form
from flask_babel import gettext
from wtforms.fields import TextField
from wtforms.validators import Length
from wtforms.ext.sqlalchemy.orm import model_form

from .models import Contact
from ..core import db


class ContactForm(Form):
    name = TextField(gettext(u'Name'))
    duty = TextField(gettext(u'Duty'))
    #department = TextField('部门')
    mobile = TextField(gettext(u'Mobile'))
    telephone =TextField(gettext(u'Telephone'))
    innerphone = TextField(gettext(u'Innerphone'))
    fax = TextField(gettext(u'Fax'))


CF = model_form(Contact,
                db_session=db.session,
                base_class=Form,
                exclude=['user', 'qq', 'name_shot', 'name_pinyin'],
                field_args ={
                    'fax':{
                        'label': gettext(u'Fax')
                    }, 'name': {
                        'label': gettext(u'Name')
                    }, 'department':{
                        'label': gettext(u'Dept')
                    }, 'duty': {
                        'label': gettext(u'Duty')
                    }, 'mobile': {
                        'label': gettext(u'Mobile')
                    }, 'telephone': {
                        'label': gettext(u'Telephone')
                    }, 'innerphone': {
                        'label': gettext(u'Innerphone')
                    }, 'description': {
                        'label': gettext(u'Description')
                    }
                })