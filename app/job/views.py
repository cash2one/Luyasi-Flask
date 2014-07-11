# -*- coding: utf-8 -*-
"""
   	$(filename)
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

import app.core
from .models import Job

class JobView(app.core.AuthModelView):
    column_list=('title',)
    def __init__(self):
        super(JobView, self).__init__(Job, app.core.db.session, name="Jobs", endpoint="jobs", category='Job')