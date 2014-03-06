#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
def import_qingbank_user(filepath=None):
    import pinyin
    import xlrd
    import uuid
    from app.services import api_contact, api_department

    book = xlrd.open_workbook('d:/2014.xls')
    sheet = book.sheets()[0]
    max_row = sheet.nrows
    print 'Begin init qingbank contact'
    name_dict = {}
    # max_row = 3
    repeat_id = []
    for i in range(1, max_row):
        print str.format('{0}/{1}', i, max_row)
        employee_id = sheet.row_values(i)[9].strip()
        desc = None
        if employee_id is None or employee_id=='':
            employee_id = str(uuid.uuid1())
            desc = u'非在编人员'
        dept_name = sheet.row_values(i)[1].strip()
        duty = sheet.row_values(i)[2].strip()
        name = sheet.row_values(i)[3].strip()
        name_pinyin = pinyin.get(name)
        name_shot = pinyin.get_initial(name, '')
        mobile = sheet.row_values(i)[4]
        if isinstance(mobile, float):
            mobile = str(int(mobile))
        mobile.strip()
        tel = sheet.row_values(i)[5]
        if isinstance(tel, float):
            tel = str(int(tel))
        tel.strip()
        fax = sheet.row_values(i)[6]
        if isinstance(fax, float):
            fax = str(int(fax))
        fax.strip()

        # 创建到数据库
        user = user_datastore.get_user(employee_id + '@qingbank.cn')
        if user is not None:
            print 'already exist the same id: ' + user.username
            user.contact.description = 'dept_name'
            repeat_id.append(user.username)
            continue
        user = user_datastore.create_user(username=employee_id, password=name_pinyin, email=employee_id + '@qingbank.cn')
        db.session.commit()
        dept = api_department.first(name=dept_name)
        if dept is None:
            dept = api_department.create(name=dept_name)

        api_contact.create(name=name,  name_pinyin=name_pinyin, name_shot=name_shot, 
                user_id=user.id, department_id=dept.id, duty=duty, mobile=mobile, telephone=tel, fax=fax, description=desc)
        
    print repeat_id

@manager.command
def init_doc_tree(dirpath=None):
    '''
    初始化树形目录结构
    '''
    from app.services import api_node
    import os
    #根目录
    dirpath = u'D:/out/法规'
#     name = os.path.split(dirpath)[1]
#     parent = api_node.create(name=name)
    print dirpath
    #入口目录作一个根节点


    #节点生成流程：
    #1.使用dirpath生成一个节点
    #2.使用filenames生成叶子节点
    #3.dirnames不作处理，等在下一次遍历时重复步骤1来完成
    parent = DocNode()
    for dirpath, dirnames, filenames in os.walk(dirpath):
        print 'dirpath:'
        print dirpath
        #link为路径，文件节点才要
        name = os.path.split(dirpath)[1]
        link = os.path.normpath(os.path.splitdrive(dirpath)[1]).replace('\\','/')
        node = api_node.create(name=name, parent_id=parent.id, link=link, is_leaf=False)
        parent = node
        # print 'dirnames:'
        # for dn in dirnames:
        #     print dn

        print 'filenames:'
        for fn in filenames:
            name = os.path.split(os.path.splitext(fn)[0])[1]
            link = os.path.join(os.path.splitdrive(dirpath)[1], os.path.splitext(fn)[0])
            link = os.path.normpath(link).replace('\\', '/')
            api_node.create(name=name,parent_id=parent.id,link=link, is_leaf=True)
            print fn
    
    print 'end'

if __name__ == '__main__':
    manager.run()
