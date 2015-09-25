#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Kinorsi --<kinorsi@gmail.com>
  Purpose: Captcha field for wtform.
  Created: 2014/6/11
"""
import datetime

from wtforms import TextField, Field, TextField, DateTimeField as WtfDateTimeField, DateField as WtfDateField
from wtforms.validators import Required
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

########################################################################
class DateTimeField(WtfDateTimeField):
      """自己重写的DateTimeField，主要是有必须填写的验证时才做格式的判断值的时候"""

      def process_formdata(self, valuelist):
            if valuelist:
                  date_str = ' '.join(valuelist)
                  if date_str.strip() == '':
                        for vali in self.validators:
                              if(isinstance(vali, Required)):
                                    try:
                                          self.data = datetime.datetime.strptime(date_str, self.format)
                                    except ValueError:
                                          self.data = None
                                          raise ValueError(self.gettext('日期格式无效'))
                  else:
                        try:
                              self.data = datetime.datetime.strptime(date_str, self.format)
                        except ValueError:
                              self.data = None
                              raise ValueError(self.gettext('日期格式无效'))


########################################################################
class DateField(WtfDateField):
      """自己重写的DateField，主要是有必须填写的验证时才做格式的判断值的时候"""

      def process_formdata(self, valuelist):
            if valuelist:
                  date_str = ' '.join(valuelist)
                  if date_str.strip() == '':
                        for vali in self.validators:
                              if(isinstance(vali, Required)):
                                    try:
                                          self.data = datetime.datetime.strptime(date_str, self.format)
                                    except ValueError:
                                          self.data = None
                                          raise ValueError(self.gettext('日期格式无效'))
                  else:
                        try:
                              self.data = datetime.datetime.strptime(date_str, self.format)
                        except ValueError:
                              self.data = None
                              raise ValueError(self.gettext('日期格式无效'))
