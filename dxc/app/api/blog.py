# -*- coding: utf-8 -*-
"""
   $(filename)
    ~~~~~~~~~~~

    Blog api

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

from flask import Blueprint, request, render_template, url_for
from flask_security import current_user

from flaskframe.helpers import mkmillseconds, jsonres
from dxc.services import api_blog
from . import paginationInfo, route
from dxc.app.models.blog import BlogForm, BlogUpdateForm

bp = Blueprint('api_blog', __name__, url_prefix='/blogs')

#----------------------------------------------------------------------
@route(bp, '/blog-new', methods=['POST'])
def create_blog():
    """"""
    blog_form = BlogForm(**request.json)
    blog_form.csrf_enabled = False
    del blog_form.captcha

    if blog_form.validate_on_submit():
        blog = api_blog.create(user=current_user, **request.json)
        return jsonres(rv=dict(id=blog.id, title=blog.title, content=blog.content))

    return jsonres(metacode=400, code=400, msg=blog_form.errors)

#----------------------------------------------------------------------
@bp.route('<matrix:blogs_matrix>', methods=['GET'])
def list_blog(blogs_matrix=dict()):
    page = int(request.args.get('page', 1));
    if page == None or page <= 0:
        page = 1
    blogs = api_blog.get_latest_page_filterby(page=page, per_page=10,
                                              category_id=int(blogs_matrix.get('category', 0)))
    pageInfo = paginationInfo(blogs)
    #这个用在动弹里的
    if blogs_matrix.get('showcontent'):
            blogdatas = [dict(id=blog.id,
                      title=blog.title,
                      content=blog.content,
                      userid = blog.user_id,
                      useravatar = blog.user.avatar or url_for('static', filename='/image/'),
                      username = blog.user.validname(),
                      create_at=mkmillseconds(blog.create_at)) for blog in blogs.items]
    else:
        blogdatas = [dict(id=blog.id,
                          title=blog.title,
                          create_at=mkmillseconds(blog.create_at)) for blog in blogs.items]
    return jsonres(rv=dict(pageInfo=pageInfo, datas=blogdatas))


#----------------------------------------------------------------------
@route(bp, '/profile_blogs/<int:category>/<int:page>', '/profile_blogs/<int:category>', methods=['GET'])
def list_profileblogs(category=0, page=1):
    """在个人中心显示自己发的blog"""
    if page == None or page <= 0:
        page = 1
    blogs = api_blog.get_latest_page_filterby(page=page, category=category, user=current_user)
    return render_template('blog/profile_blogs.html', blogs = blogs, category=category)

#----------------------------------------------------------------------
@route(bp, '/blog-<int:blog_id>', methods=['DELETE'])
#@right_require('blog')
def delete_blog(blog_id):
    """Delete blog.
    :param id: blog id.
    """
    blog = api_blog.get(blog_id)
    if blog.user != current_user:
        return jsonres(rv=None, metacode=403, msg=u'这不是您的，你不能删除', code=403)

    api_blog.delete(api_blog.get_or_404(blog_id))
    return jsonres()

#----------------------------------------------------------------------
@route(bp, '', methods=['DELETE'])
#@right_require('blog')
def delete_blogs():
    """Delete blog.
    :param id: blog id.
    """
    delIds = request.json
    for delId in delIds:
        blog = api_blog.get(delId)
        if blog.user != current_user:
            return jsonres(metacode=403, msg=u'有不是您的，不能删除', code=403)

    return jsonres()


#----------------------------------------------------------------------
@route(bp, '/blog-<int:blog_id>', methods=['POST'])
def change_blog(blog_id):
    """Edit the blog.
    :param id: blog id.
    """
    blog = api_blog.get(blog_id)
    if blog.user != current_user:
        return jsonres(rv=None, metacode=403, msg=u'这不是您的，你不能修改', code=403)

    blog_form = BlogUpdateForm()
    #json方式，不能验证csrf_token
    blog_form.csrf_enabled = False

    if blog_form.validate_on_submit():
        api_blog.update(blog, **blog_form.data)
        return jsonres()

    #构造表单验证错误，返回
    return jsonres(msg=blog_form.errors, metacode=400, code=400)

#----------------------------------------------------------------------
@bp.route('/blog-<int:blog_id>', methods=['GET'])
def detail_blog(blog_id):
    blog = api_blog.get_or_404(blog_id)
    return jsonres(rv=dict(id=blog.id, title=blog.title, content=blog.content, create_at=mkmillseconds(blog.create_at)))