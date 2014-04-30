#-*- coding:utf-8 -*-

#这个类用来调试打断点用的。因为直接启动test方法会没有环境。

import unittest
from tests.frontend.qingbank_tests import QingbankFrontendTestCase

if __name__ == '__main__':
	unittest.main()