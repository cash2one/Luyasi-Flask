# -*- coding: utf-8 -*-
"""
  	Models for taste.
	~~~~~~~~~~~

    :copyright: (c) 2016 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

from flaskframe.core import db, ModelVersion
from flaskframe.helpers import JsonSerializer


class Shop(db.Model, ModelVersion, JsonSerializer):
    """店铺
    """
    __tablename__="taste_shop"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    desc = db.Column(db.String(200))
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship('User', backref=db.backref('shops', uselist=True, lazy='dynamic'))

    def __repr__(self):
        return str.format('<TasteShop: {}>', self.name)

    def __str__(self):
        return  u'%s' % self.name

class Item(db.Model, ModelVersion, JsonSerializer):
    """产品
    """
    __tablename__='taste_item'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(), nullable=False, default=0.0)
    desc = db.Column(db.Text())
    shop_id =db.Column(db.Integer(), db.ForeignKey(Shop.id))
    shop = db.relationship(Shop, backref=db.backref('items', uselist=True, lazy='dynamic'))

    def __repr__(self):
        return str.format('<TasteItem: {}>', self.name)

    def __str__(self):
        return  u'%s' % self.name
