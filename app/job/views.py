# -*- coding: utf-8 -*-
"""
   	$(filename)
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

import app.core
from .models import Job
from ..framework.ckeditor import CKEditorField

class JobView(app.core.AuthModelView):
    column_list=('title',)
    form_overrides=dict(content=CKEditorField)
    form_args = {
        'content': {
            'import_js': True
        }
    }    
    def __init__(self):
        super(JobView, self).__init__(Job, app.core.db.session, name="Jobs", endpoint="jobs", category='Job')