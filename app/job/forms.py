# -*- coding: utf-8 -*-
"""
   	Job forms.
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

from flask_wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField, TextAreaField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required, Length
from flask_babel import gettext, lazy_gettext

from ..framework.ckeditor import CKEditorField, CKEditorRequired
from ..framework.wtfext.fields import CaptchaField

########################################################################
class JobForm(Form):
	id = IntegerField(u'id', default=0, widget=HiddenInput())
	title = TextField(lazy_gettext(u'Title'), validators=[Required()])
	job_type = SelectField(gettext(u'Job type'), choices=[(0, lazy_gettext(u'Part time job')), (1, lazy_gettext(u'Full time job'))], coerce=int)
	content = CKEditorField(lazy_gettext(u'Job detail'), import_js=True, validators=[CKEditorRequired(message=gettext('The comment forgot you~'))],
	                        ckeditor_config_file_path='base/ckeditor-job-config.js')
	captcha = CaptchaField()


########################################################################
class JobReportForm(Form):
	"""Form for reporting a job"""

	id = IntegerField(u'id', default=0, widget=HiddenInput())
	content = TextAreaField(lazy_gettext(u'Report content'), validators=[Required(), Length(min=30)])
	captcha = CaptchaField()

