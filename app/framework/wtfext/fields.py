#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Kinorsi --<kinorsi@gmail.com>
  Purpose: Captcha field for wtform.
  Created: 2014/6/11
"""

from wtforms import TextField, Field
from flask_babelex import lazy_gettext

from .widgets import CaptchaWidget
from .validators import ValidCaptcha

########################################################################
class CaptchaField(Field):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, description=None, **kwagrs):
		description = description or lazy_gettext(u'repeat captcha')
		super(CaptchaField, self).__init__(validators=(ValidCaptcha(),), label=lazy_gettext(u'captcha'), description=description, **kwagrs)
		self.widget = CaptchaWidget()




