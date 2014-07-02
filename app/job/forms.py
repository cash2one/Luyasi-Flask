# -*- coding: utf-8 -*-
"""
   	Job forms.
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

from flask_wtf import Form
from wtforms.fields import TextField, HiddenField, SelectField
from wtforms.validators import Required, Length
from flask_babel import gettext

from ..framework.ckeditor import CKEditorField, CKEditorRequired
from ..framework.wtfext.fields import CaptchaField

########################################################################
class JobForm(Form):
	id = HiddenField(u'id', default=None)
	title = TextField(gettext(u'Title'), validators=[Required()])
	job_type = SelectField(gettext(u'Job type'), choices=[(0, gettext(u'Part time job')), (1, gettext(u'Full time job'))], coerce=int)
	content = CKEditorField(gettext(u'Detail'), import_js=True, validators=[CKEditorRequired(message=gettext('The comment forgot you~'))],
	                        ckeditor_config_file_path='base/ckeditor-job-config.js')
	captcha = CaptchaField()