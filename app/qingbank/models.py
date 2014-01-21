#-*- coding:utf-8 -*-
from ..core import db
from ..helpers import JsonSerializer


class Department(db.Model, JsonSerializer):
	"""docstring for QBDepartment"""
	__tablename__ = 'qingbank_department'
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(20), unique=True)
	address = db.Column(db.String(255))
	def __repr__(self):
		return self.name


class Contact(db.Model, JsonSerializer):
	"""docstring for QBContactInfo"""

	# __json_hidden__ = ['department']
	__tablename__ = 'qingbank_contact'
	
	id = db.Column(db.Integer(), primary_key=True)
	employee_no = db.Column(db.String(10))
	name = db.Column(db.String(10))
	name_pinyin = db.Column(db.String(30))
	name_shot = db.Column(db.String(10))
	duty = db.Column(db.String(10))
	mobile = db.Column(db.String(14))
	telephone = db.Column(db.String(20))
	innerphone = db.Column(db.String(20))
	fax = db.Column(db.String(14))
	qq = db.Column(db.String(20))
	department_id = db.Column(db.Integer(), db.ForeignKey('qingbank_department.id'))
	department = db.relationship('Department', backref=db.backref('contacts', lazy='dynamic'))
	# user = db.relationship('User', backref=db.backref('contact', lazy='dynamic'))
	def __repr__(self):
          return '<Contact %r>' % (self.name)
