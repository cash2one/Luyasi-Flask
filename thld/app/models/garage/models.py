# -*- coding: utf-8 -*-
from flaskframe.core import db, ModelVersion
from flaskframe.helpers import JsonSerializer
from flaskframe.security.models import User

__author__ = 'kinorsi'


# ==============车位出租==================================
class GarageRent(db.Model, ModelVersion, JsonSerializer):
    __tablename__ = 'garage_garagerent'

    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.Float())
    # 位置
    position = db.Column(db.String(20))
    contact = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    # 关闭，不再求租
    close = db.Column(db.Boolean(name='close'), default=False, nullable=False)
    # 备注
    desc = db.Column(db.String(100))
    read = db.Column(db.Integer(), default=0)

    # 发布人
    publisher_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    publisher = db.relationship(User, backref=db.backref('garageRents', uselist=True, lazy='dynamic'))

    def __repr__(self):
        return u'<GarageRent: %s>', self.id

    def __str__(self):
        return u'%s' % self.id
