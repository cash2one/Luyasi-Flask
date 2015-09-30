#-*- coding:utf-8 -*-

from dxc.tests import LuyasiTestCase
from dxc.tests import test_setting
from dxc.app import api


class LuyasiApiTestCase(LuyasiTestCase):
    def create_app(self):
        #这个要是写在最前面会和test下的front混在一起。。		
        app = api.create_app(settings_override=test_setting)
        app.config['TESTING'] = True
        return app