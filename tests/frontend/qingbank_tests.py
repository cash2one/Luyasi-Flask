# -*- coding:utf-8 -*-

#这个文件用来做一些factory的使用测试。给其它进行参考。

from tests.factories import ContactFactory

from . import LuyasiFrontendTestCase


class QingbankFrontendTestCase(LuyasiFrontendTestCase):

    render_templates  = True

    def _create_fixtures(self):
        super(QingbankFrontendTestCase, self)._create_fixtures()
        ContactFactory()
        ContactFactory()

    def test_index(self):
        self.get('/qingbank/')
        self.assert_template_used('qingbank/index.html')

    def test_list_contact_page(self):
        self.get('/qingbank/contacts/1')
        contacts = self.get_context_variable('contacts')
        self.assertEqual(contacts.total, 2)

    def test_contact_detail(self):
        c1 = ContactFactory(name=u'黄展旗', name_pinyin=u'huangzhanqi', name_shot=u'hzq')
        self.get('/qingbank/contact/' + str(c1.id))
        self.assertContext('contact', c1)




