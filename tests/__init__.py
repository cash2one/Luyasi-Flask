# -*- coding:utf-8 -*-

from flask.ext.testing import TestCase

from app.core import db
from tests.factories import UserFactory, RoleFactory
from tests.utils import FlaskTestCaseMixin

from datetime import datetime


class LuyasiTestCase(TestCase, FlaskTestCaseMixin):
	def setUp(self):
		db.create_all()
		self._create_fixtures()
		self._create_csrf_token()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def _create_fixtures(self):
		"""创建初始数据"""
		r = RoleFactory(name=u'管理员')	
		self.user = UserFactory(email='kinorsi', password='luyasi', confirmed_at=datetime.now(), active=True, roles=(r,))

   	def _login(self, email=None, password=None):
   		"""登陆，并保存了cookies"""
		email = email or self.user.email
		password = password or self.user.password or 'password'
		login_res = self.post('/security/login', data={'email': email, 'password': password}, follow_redirects=True)	
		headers = login_res.headers
		
		cookies = self.getCookies(login_res)
		self.cookies = cookies




