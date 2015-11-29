# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms.fields import IntegerField, FloatField, StringField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired


class GarageForm(Form):
    id = IntegerField(u'id', default=0, widget=HiddenInput())
    price = FloatField(u'出租价格', validators=[DataRequired(u'请输入出租价格')])
    position = StringField(u'位置', validators=[DataRequired(u'请输入位置信息')])
    contact = StringField(u'联系人', validators=[DataRequired(u'请输入联系人')])
    phone = StringField(u'联系电话', validators=[DataRequired(u'请输入联系电话')])
    desc = StringField(u'其它说明')
