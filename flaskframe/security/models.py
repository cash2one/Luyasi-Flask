# -*- coding:utf-8 -*-
from flask.ext.security import RoleMixin, UserMixin

from flaskframe.helpers import JsonSerializer
from flaskframe.core import db, ModelVersion

# 用在Flask-Security里的
users_roles = db.Table('security_users_roles',
                       db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('security_role.id')))
# 用来记录应用和用户的关系
users_apps = db.Table('security_users_apps',
                      db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id')),
                      db.Column('app_id', db.Integer(), db.ForeignKey('security_app.id')))

users_rights = db.Table('security_users_rights',
                        db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id')),
                        db.Column('right_id', db.Integer(), db.ForeignKey('security_right.id')))

roles_rights = db.Table('security_roles_rights',
                        db.Column('role_id', db.Integer(), db.ForeignKey('security_role.id')),
                        db.Column('right_id', db.Integer(), db.ForeignKey('security_right.id')))


########################################################################
class Role(db.Model, ModelVersion, RoleMixin, JsonSerializer):
    __tablename__ = 'security_role'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    rights = db.relationship('Right', secondary=roles_rights, lazy='dynamic')

    def __repr__(self):
        return u'<Role: %s>' % self.name

    def __str__(self):
        return u'%s' % self.name


########################################################################
class User(db.Model, ModelVersion, UserMixin, JsonSerializer):
    # 关于user的名字要描述一下：user有nickname, username, email这些基本的，然后还会有其它模块的信息如个人中心的真实名字。
    __tablename__ = 'security_user'
    __json_hidden__ = ['blogs', 'contact', 'password']

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(name='active'), default=True)
    nickname = db.Column(db.String(80))
    avatar = db.Column(db.String(255))

    # openid登陆后可以绑定旧有的帐号
    bind_username = db.Column(db.String(255))
    bind_email = db.Column(db.String(80))
    # 下次提醒
    bind_remind = db.Column(db.Boolean(name='bind_remind'))
    # use for openid
    openid = db.Column(db.String(80))
    provider = db.Column(db.String(20))
    # openid and provider should be unique. 命名规则和sqlalchem metadata一样。
    __table_args__ = (db.UniqueConstraint('openid', 'provider', name='uq__user__openid__provider'),)

    # Many items belong to the user
    roles = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))
    apps = db.relationship('App', secondary=users_apps, lazy='dynamic')
    rights = db.relationship('Right', secondary=users_rights, lazy='dynamic')

    # 要打开SECURITY_TRACKABLE
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(80))
    current_login_ip = db.Column(db.String(80))
    login_count = db.Column(db.Integer())

    def __repr__(self):
        return '<User: %s>' % (self.username or self.email or self.nickname)

    def __str__(self):
        return u'%s' % (self.username or self.email or self.nickname)

    def validname(self):
        return u'%s' % (self.nickname or self.username or self.email)

    def canAdmin(self):
        for role in self.roles:
            if u'管理员' in role.name:
                return True
        return False


########################################################################
class App(db.Model, ModelVersion, JsonSerializer):
    __tablename__ = 'security_app'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    app_version = db.Column(db.String(32))
    app_vercode = db.Column(db.Integer())
    update_url = db.Column(db.String(255))

    def __repr__(self):
        return u'<App: %s>', self.name

    def __str__(self):
        return u'%s' % self.name


########################################################################
class Right(db.Model, ModelVersion, JsonSerializer):
    __tablename__ = 'security_right'

    id = db.Column(db.Integer(), primary_key=True)
    action = db.Column(db.String(50))
    app = db.Column(db.String(50))
    entity = db.Column(db.String(50))
    description = db.column_property(action + ' ' + app + ' ' + entity)

    def __repr__(self):
        return u'<Right: %s>', self.description

    def __str__(self):
        return u'%s' % self.description


class SysMessage(db.Model, ModelVersion, JsonSerializer):
    """系统通知"""
    __tablename__ = 'security_sysmessage'
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(512), nullable=False)
    is_read = db.Column(db.Boolean(name="is_read"), default=False, nullable=False)
    receiver_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    receiver = db.relationship(User, backref=db.backref('sys_messages'))
