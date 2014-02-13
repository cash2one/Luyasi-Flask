#-*- coding:utf-8 -*-

from app import config
# from app.core import db
from app.helpers import import_model

from flask import Flask
from flask.ext.script import Manager, prompt_bool
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
#我去，这个放在这里是因为model里用到了db
from app.qingbank.models import *
from app.security.models import *

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
#: Flask-Script instance
manager = Manager(app)


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

@manager.command
def create_user(username, email, password):
    "Creates a user with username and password"
    user_datastore.create_user(
        email=email, password=password, username=username)
    db.session.commit()


@manager.command
def import_qingbank_user(filepath):
    import pinyin
    import xlrd
    from app.services import api_contact, api_department

    book = xlrd.open_workbook('d:/e.xls')
    sheet = book.sheets()[0]
    max_row = sheet.nrows
    print 'Begin init qingbank contact'
    name_dict = {}
    # max_row = 3
    for i in range(1, max_row):
        print 'row', i
        employee_id = sheet.row_values(i)[0].strip()
        name = sheet.row_values(i)[2].strip()
        name_pinyin = pinyin.get(name)
        name_shot = pinyin.get_initial(name, '')

        # 创建到数据库
        user = user_datastore.create_user(username=employee_id, password=name_pinyin)
        db.session.commit()

        api_contact.create(name=name,  name_pinyin=name_pinyin, name_shot=name_shot, user_id=user.id)


if __name__ == '__main__':
    manager.run()
