#-*- coding:utf-8 -*-
from flask.ext.security import RoleMixin, UserMixin
from flask.ext.babel import gettext
from ..core import db

# 用在Flask-Security里的
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    def __repr__(self):
        # return str.format('<Role {0}>', self.name)
        return gettext(u'%(value)s', value=self.name)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    # contact = db.relationship('Contact', backref='user', uselist=True)

    # 要有邮件服务器才能使用
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(80))
    current_login_ip = db.Column(db.String(80))
    login_count = db.Column(db.Integer())
    def __repr__(self):
        return gettext(u'%(value)s', value=self.username or self.email)
