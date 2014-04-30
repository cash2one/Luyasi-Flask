# -*- coding:utf-8 -*-

# 这个文件用来做一些factory的使用测试。给其它进行参考。

from . import LuyasiApiTestCase
from app.security.models import User, Role
from tests.factories import UserFactory, RoleFactory, ContactFactory

class QingbankApiTestCase(LuyasiApiTestCase):

	render_templates = False

	def setUp(self):
		super(QingbankApiTestCase, self).setUp()
 		self._login()


		
