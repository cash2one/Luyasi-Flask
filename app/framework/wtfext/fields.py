#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Kinorsi --<kinorsi@gmail.com>
  Purpose: Captcha field for wtform.
  Created: 2014/6/11
"""

from wtforms import TextField, Field

from .widgets import CaptchaWidget
from .validators import ValidCaptcha

########################################################################
class CaptchaField(Field):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, **kwagrs):
		super(CaptchaField, self).__init__(validators=(ValidCaptcha(),), **kwagrs)
		self.widget = CaptchaWidget()




