#-*- coding:utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Length

class ContactForm(Form):
	# employee_no = TextField()
	name = TextField('名字')
	# duty = db.Column(db.String(10))
	mobile = TextField('移动电话')
	telephone =TextField('固话')
	innerphone = TextField('内线')
	fax = TextField('传真')
	qq = TextField('QQ')
	# department_id = db.Column(db.Integer(), db.ForeignKey('qingbank_department.id'))
	# department = db.relationship('Department', backref=db.backref('contacts', lazy='dynamic'))	

