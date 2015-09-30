# # -*- coding:utf-8 -*-
# 
# #这个文件用来做一些factory的使用测试。给其它进行参考。使用时全选并把注释去掉。
# 
# import unittest
# 
# from . import LuyasiApiTestCase
# from dxc.core import db
# from dxc.security.models import User, Role
# from tests.factories import UserFactory, RoleFactory,ContactFactory
# 
# class SampleTestCase(LuyasiApiTestCase):
# 
# 	render_templates  = False
# 
# 	def test_list_contacts(self):
# 		# response = self.client.get('/qingbank/contact', follow_redirects=True)
# 		# print 'data',response.data
# 		# assert "" == response.data
# 		# security = self.client.application.extensions['security']
# 		# store = security.datastore
# 		# u = UserFactory.attributes()
# 		# u1 = store.create_user(**u)
# 		# user = store.find_user(email='user_2@qb.cn')
# 
# 		# 测试manytomany的效果
# 		r  = RoleFactory(name=u'管理员')	
# 		r2 = RoleFactory(name=u'打酱油')
# 		u = UserFactory(roles=(r,r2))
# 
# 
# 		print db.session.query(User).get(1).roles[0].name
# 		db.session.commit()
# 		# print db.session.query(Role).get(1)
# 		db.session.query(User).count()
# 
# 	def test_contacts(self):
# 		"""测试foreign key的使用方法"""
# 		u = UserFactory(username='kinorsi')
# 		c = ContactFactory(user=u)
# 		print c.department
# 		print c.user, c.user.id
# 
# 		