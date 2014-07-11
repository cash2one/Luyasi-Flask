# -*- coding: utf-8 -*-
"""
   	$(filename)
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

import app.core
from .models import Blog, Comment

class BlogView(app.core.AuthModelView):

    column_list=('title',)
    def __init__(self):
        super(BlogView, self).__init__(Blog, app.core.db.session, name="Blogs", endpoint="blogs", category='Blog')

class CommentView(app.core.AuthModelView):

    column_list=('content',)
    def __init__(self):
        super(CommentView, self).__init__(Comment, app.core.db.session, name="Comments", endpoint="comments", category='Blog')
