#-*- coding: utf-8 -*-

from ..core import db, ModelVersion
from ..helpers import JsonSerializer

from ..security.models import User

academies_classes = db.Table('xiaoyuan_academies_classes',
                       db.Column('academy_id', db.Integer(), db.ForeignKey('xiaoyuan_academy.id')),
                       db.Column('class_id', db.Integer(), db.ForeignKey('xiaoyuan_class.id')))

academies_users = db.Table('xiaoyuan_academies_users',
                       db.Column('academy_id', db.Integer(), db.ForeignKey('xiaoyuan_academy.id')),
                       db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id')))

classes_users = db.Table('xiaoyuan_classes_users',
                       db.Column('class_id', db.Integer(), db.ForeignKey('xiaoyuan_class.id')),
                       db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id'))) 


########################################################################
class Academy(db.Model, ModelVersion, JsonSerializer):
    __tablename__ = 'xiaoyuan_academy'
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    
    #这个学院的人。主要是用来在领导的
    users = db.relationship(User, secondary=academies_users, backref=db.backref('academies', lazy='dynamic'))

########################################################################
class Class(db.Model, ModelVersion, JsonSerializer):
    """"""
    __tablename__ = "xiaoyuan_class"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    
    # 在这个班的人
    users = db.relationship(User, secondary=classes_users, backref=db.backref('classes', lazy='dynamic'))
    
    # 这个班所在的学院
    academy_id = db.Column(db.Integer(), db.ForeignKey('xiaoyuan_academy.id'))
    academy = db.relationship('Academy', backref=db.backref('classes', uselist=True, lazy='dynamic'))    
        
class Message(db.Model, ModelVersion, JsonSerializer):
    
    __tablename__ = "xiaoyuan_message"
    
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(256))
    
    sender_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    sender = db.relationship('User', backref=db.backref('send_msgs', uselist=True, lazy='dynamic'),
                             foreign_keys=[sender_id])
    
    receiver_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    receiver = db.relationship('User', backref=db.backref('receive_msgs', uselist=True, lazy='dynamic'),
                               foreign_keys=[receiver_id])    