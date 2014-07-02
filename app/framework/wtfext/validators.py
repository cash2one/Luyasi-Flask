#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Kinorsi --<>
  Purpose:
  Created: 2014/6/12
"""
from wtforms import ValidationError
from flask import session
from flask_babel import gettext

class ValidCaptcha(object):
    """Validate the captcha"""
    def __init__(self, message=None):
        if not message:
            message = gettext(u"Captcha is not valid")
        self.message = message

    def __call__(self, form, field):
        code = field.data
        if session.get('captcha') is None or code.upper() != session.get('captcha'):
            raise ValidationError(self.message)
        elif 'captcha' in session:
            session.pop('captcha')


