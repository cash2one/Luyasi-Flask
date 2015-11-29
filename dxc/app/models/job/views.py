# -*- coding: utf-8 -*-
"""
   	$(filename)
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

import flaskframe.core
from .models import Job
from flaskframe.ckeditor import CKEditorField

class JobView(flaskframe.core.AuthModelView):
    column_list=('title',)
    form_overrides=dict(content=CKEditorField)
    form_args = {
        'content': {
            'import_js': True
        }
    }    
    def __init__(self):
        super(JobView, self).__init__(Job, flaskframe.core.db.session, name=u"工作", endpoint="jobs", category=u'工作管理')