#-*- coding:utf-8 -*-
from flask.ext.script import Manager, prompt_bool
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask import Flask
from app import config
from app.core import db
from app.security.models import User, Role

from app.helpers import import_model

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
#: Flask-Script instance
manager = Manager(app)

#引入model进行处理
from app.qingbank.models import *
from app.security.models import *

@manager.command
def test():
	from app.qingbank.models import Contact
	print 'isinstance: %s' % isinstance(Contact, db.Model)
	print 'issubclass: %s' % issubclass(Contact, db.Model)
	
@manager.command
def create_db():
	"Creates all database tables"
	print 'syncing...'
	db.create_all()
	print 'synchronization finished'

@manager.command
def drop_db():
	"Drops all the databse tables"
	if prompt_bool("Are you sure to drop your databse?"):
		print 'Droping databse'
		db.drop_all()
		print 'Droping finished'

# 不工作
@manager.command
def create_user(username, password):
	"Creates a user with username and password"
	# if username==None or password==None:
	# 	print 'username / password is empty'
	# 	return
	user_datastore.create_user(email=username, password=password)
	db.session.commit()

if __name__ == '__main__':
	manager.run()