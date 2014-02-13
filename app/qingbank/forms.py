#-*- coding:utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Length
from wtforms.ext.sqlalchemy.orm import model_form

from .models import Contact
from ..core import db


class ContactForm(Form):
	name = TextField('名字')
	duty = TextField('职务')
	#department = TextField('部门')
	mobile = TextField('移动电话')
	telephone =TextField('办公电话')
	innerphone = TextField('内线')
	fax = TextField('传真')


CF = model_form(Contact, 
	db_session=db.session, 
	base_class=Form,
	exclude=['user', 'qq', 'name_shot', 'name_pinyin'],
	field_args ={
	 	'fax':{
	 		'label': '传真'
	 	}, 'name': {
	 		'label': '名字'
	 	}, 'department':{
	 		'label': '部门'
	 	}, 'duty': {
	 		'label': '职务'
	 	}, 'mobile': {
	 		'label': '移动电话'
	 	}, 'telephone': {
	 		'label': '办公电话'
	 	}, 'innerphone': {
	 		'label': '内线'
	 	}
	})