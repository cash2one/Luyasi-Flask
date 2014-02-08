#-*- coding:utf-8 -*-
from ..core import db
from ..helpers import JsonSerializer

class  Loupan(db.Model, JsonSerializer):
	"""docstring for QBDepartment"""
	__tablename__ = 'home_loupan'

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(20), unique=True)
	address = db.Column(db.String(255))
	def __repr__(self):
		return self.name
