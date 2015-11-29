# -*- coding: utf-8 -*-
"""
   	$(filename)
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

import flaskframe.core
from .models import Blog, Comment, Category
from flaskframe.ckeditor import CKEditorField


class BlogView(flaskframe.core.AuthModelView):
    column_list = ('title',)
    form_overrides = dict(content=CKEditorField)
    form_args = {
        'content': {
            'import_js': True
        }
    }

    def __init__(self):
        super(BlogView, self).__init__(Blog, flaskframe.core.db.session,
                                       name=u"文章",
                                       endpoint="blogs",
                                       category=u'文章管理')


class CommentView(flaskframe.core.AuthModelView):
    column_list = ('content',)

    def __init__(self):
        super(CommentView, self).__init__(Comment, flaskframe.core.db.session,
                                          name=u"评论",
                                          endpoint="comments",
                                          category=u'文章管理')


class CategoryView(flaskframe.core.AuthModelView):
    column_list = ('name',)

    def __init__(self):
        super(CategoryView, self).__init__(Category, flaskframe.core.db.session,
                                           name=u"栏目",
                                           endpoint="Categories",
                                           category=u'文章管理')
