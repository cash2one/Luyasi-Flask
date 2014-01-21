# -*- coding: utf-8 -*-
import os
from pprint import pprint

from flask import *

from app import *


# import readline
os.environ['PYTHONINSPECT'] = 'True'

def init_db():
	import app
	myapp = app.api.create_app()
	from flask.ext.sqlalchemy import SQLAlchemy
	from app.core import db
	db = SQLAlchemy(myapp)
	from app.qingbank.models import Contact, Department
	db.create_all()