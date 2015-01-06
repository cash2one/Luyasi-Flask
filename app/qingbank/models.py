#-*- coding:utf-8 -*-
from ..core import db, ModelVersion
from ..helpers import JsonSerializer


class Department(db.Model, ModelVersion, JsonSerializer):
    """docstring for QBDepartment"""
    __tablename__ = 'qingbank_department'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(255))

    def __repr__(self):
        return str.format('<Department {}>', self.name)
    
    def __str__(self):
        return  u'%s' % self.name



class Contact(db.Model, ModelVersion, JsonSerializer):
    """docstring for QBContactInfo"""
    # __json_hidden__ = ['department']
    __tablename__ = 'qingbank_contact'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(10))
    name_pinyin = db.Column(db.String(30))
    name_shot = db.Column(db.String(10))
    duty = db.Column(db.String(10))
    mobile = db.Column(db.String(14))
    telephone = db.Column(db.String(20))
    innerphone = db.Column(db.String(20))
    fax = db.Column(db.String(14))
    qq = db.Column(db.String(20))
    description = db.Column(db.String(50))

    department_id = db.Column(db.Integer(), db.ForeignKey('qingbank_department.id'))
    department = db.relationship('Department', backref=db.backref('contacts', lazy='dynamic'))

    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship('User', backref=db.backref('contact', uselist=False))

    def __repr__(self):
        return str.format('<Contact {}>', self.name)

    
    def __str__(self):
        return  u'%s' % self.name    


class DocNode(db.Model, ModelVersion, JsonSerializer):
    """Node for document"""
    __tablename__ = 'qingbank_doc'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    link = db.Column(db.String(255))
    order = db.Column(db.Integer(), default=0)
    is_leaf = db.Column(db.Boolean(name='is_leaf'), default=False)
    parent_id = db.Column(db.Integer(), db.ForeignKey('qingbank_doc.id'))
    parent = db.relationship('DocNode', remote_side=[id], backref='children')

    def __repr__(self):
        return str.format('<DocNode {}>', self.name)
    
    def __str__(self):
        return  u'%s' % self.name    