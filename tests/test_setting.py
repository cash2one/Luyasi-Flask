#-*- coding:utf-8 -*-
import os

DEBUG = False
TESTING = True

#flask - sqlalchemy 的配置
SQLALCHEMY_POOL_SIZE = None
SQLALCHEMY_POOL_TIMEOUT = None
SQLALCHEMY_POOL_RECYCLE = None

# 使用内存
#SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:qingbank@localhost/luyasi-flask-db?charset=utf8&use_unicode=0'
#使用文件，但是在没有commit的时候，文件里也不会有内容的。
# _basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'test.db')

#测试的时候就不用了, 要用的话算法有点奇怪。
WTF_CSRF_ENABLED = False