#-*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms.fields import StringField


class WishForm(Form):

    name = StringField(u'我的名字')
    content = StringField(u'祝福语')

