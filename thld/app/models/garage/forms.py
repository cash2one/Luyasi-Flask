# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms.fields import IntegerField, FloatField, StringField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.orm import model_form

from flaskframe.core import db
from .models import GarageRent

GarageForm = model_form(GarageRent,
                        db_session=db,
                        base_class=Form,
                        only=['price', 'position', 'contact', 'phone', 'desc'])

class GarageForm2(Form):
    price = FloatField(u'出租价格', validators=[DataRequired(u'请输入出租价格')])
    position = StringField(u'位置', validators=[DataRequired(u'请输入位置信息')])
    contact = StringField(u'联系人', validators=[DataRequired(u'请输入联系人')])
    phone = StringField(u'联系电话', validators=[DataRequired(u'请输入联系电话')])
    desc = StringField(u'其它说明')
