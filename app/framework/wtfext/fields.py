#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Kinorsi --<kinorsi@gmail.com>
  Purpose: Captcha field for wtform.
  Created: 2014/6/11
"""

from wtforms import TextField, Field, TextField
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


########################################################################
class Select2Field(TextField):
	""""""

	def process_formdata(self, valuelist):
		if valuelist:
			try:
				strvalues = valuelist[0].split(',')
				values = [int(v) for v in strvalues]
				self.data = values
			except (ValueError):
				self.data = None
				raise ValueError(self.gettext('Not a valid int array value'))		
    
	


