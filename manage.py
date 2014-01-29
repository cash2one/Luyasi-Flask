#-*- coding:utf-8 -*-
from app import config
from app.core import db
from app.helpers import import_model
from app.qingbank.models import *
from app.security.models import *
from flask import Flask
from flask.ext.script import Manager, prompt_bool
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
#: Flask-Script instance
manager = Manager(app)

#引入model进行处理

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

@manager.command
def recreate_db():
	"Drops all the databse tables and recreate it"
	if prompt_bool("Are you sure to drop your databse?"):
		print 'Droping database'
		db.drop_all()
		print 'Droping finished'
		print "Creating database"
		db.create_all()
		print 'Create finished'
		


# 不工作
@manager.command
def create_user(username, email, password):
	"Creates a user with username and password"
	user_datastore.create_user(email=email, password=password, username=username)
	db.session.commit()

if __name__ == '__main__':
	manager.run()
