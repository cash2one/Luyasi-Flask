#-*- coding:utf-8 -*-

from tests import LuyasiTestCase
from tests import test_setting
from app import frontend

class LuyasiFrontendTestCase(LuyasiTestCase):
    def create_app(self):
        #这个要是写在最前面会和test下的front混在一起。。
        try:
            app = frontend.create_app(settings_override=test_setting)
            app.config['TESTING'] = True
            return app
        except Exception as e:
            print e

    def setUp(self):
        super(LuyasiFrontendTestCase, self).setUp()
        #self._login()
        self._login_ajax()