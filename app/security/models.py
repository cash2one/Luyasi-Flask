#-*- coding:utf-8 -*-
from flask.ext.security import RoleMixin, UserMixin
from flask.ext.babel import gettext
from ..core import db

# 用在Flask-Security里的
roles_users = db.Table('security_roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('security_role.id')))

class Role(db.Model, RoleMixin):
    __tablename__ = 'security_role'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    def __repr__(self):
        return str.format('<Role {}>', self.name)

class User(db.Model, UserMixin):
    __tablename__ = 'security_user'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(name='active'))
    nickname = db.Column(db.String(80))

    #openid登陆后可以绑定旧有的帐号
    bind_username = db.Column(db.String(255))
    bind_email = db.Column(db.String(80))
    # use for openid
    openid = db.Column(db.String(80))
    provider = db.Column(db.String(20))
    #openid and provider should be unique. 命名规则和sqlalchem metadata一样。
    __table_args__ = (db.UniqueConstraint('openid', 'provider', name='uq__user__openid__provider'),)

    # 要有邮件服务器才能使用
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(80))
    current_login_ip = db.Column(db.String(80))
    login_count = db.Column(db.Integer())

    def __repr__(self):
        return str.format('<User {0}>',  self.username or self.email or self.nickname)

    def canAdmin(self):
        for role in self.roles:
            if '管理员' in role.name:
                return True
        return False