#-*- coding:utf-8 -*-
from flaskframe.core import db, ModelVersion
from flaskframe.helpers import JsonSerializer


class Wish(db.Model, ModelVersion, JsonSerializer):
    __tablename__ = 'wish_wish'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20))
    content = db.Column(db.String(255))

    def __repr__(self):
        return str.format('<Wish {}>', self.id)

    def __str__(self):
        return  u'%s' % self.id