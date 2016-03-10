# -*- coding:utf-8 -*-
import json

from flask import current_app, abort, flash
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import current_user
from flask_babel import gettext
import requests

from . import route
from dxc.services import api_blog, api_comment, api_category
from dxc.app.models.blog import BlogForm, CommentForm

bp = Blueprint('blog', __name__, template_folder='templates', static_folder='static', url_prefix='/blogs')


# --------------------------------------------------------
@route(bp, '/new2/<int:category>', methods=['GET', 'POST'])
# @right_require('blog')
def create_blog2(category):
    # 此处category并没有使用，只是传递一下。用在界面上
    blog_form = BlogForm(category=category)
    if blog_form.validate_on_submit():
        payload = json.dumps(blog_form.data)
        r = requests.post('http://127.0.0.1:5000/api/blog/create', json=payload)
        res = r.json()
        print res[u'method']
        flash(u'创建成功')
        return redirect(url_for('.list_blog', category=category))
    if request.method == 'POST':
        flash(u'创建失败，请检查', category='danger')
    return render_template('blog/create.html', blog_form=blog_form, category=category,
                           action_url=url_for('.create_blog', category=category))


@route(bp, '/new/<int:category>', methods=['GET', 'POST'])
# @right_require('blog')
def create_blog(category):
    # 此处category并没有使用，只是传递一下。用在界面上
    blog_form = BlogForm(category_id=category)
    cate_name = api_category.get(category)
    if blog_form.validate_on_submit():
        can_publish = 1
        if cate_name.name == u'通知通告':
            can_publish = 1
            flash(u'请等待审核')
        blog = api_blog.create(user=current_user, can_publish=can_publish, **blog_form.data)
        flash(u'创建成功')
        return redirect(url_for('.list_blog', category=category))
    if request.method == 'POST':
        flash(u'创建失败，请检查', category='danger')
    return render_template('blog/create.html', blog_form=blog_form, category=category,
                           action_url=url_for('.create_blog', category=category))


# --------------------------------------------------------
@bp.route('/blogs/<int:category>/<int:page>', methods=['GET'])
@bp.route('/blogs/<int:category>/', methods=['GET'])
def list_blog(category=0, page=1):
    if page == None or page <= 0:
        page = 1
    blogs = api_blog.get_latest_page_filterby(page=page, category_id=category, can_publish=1)
    return render_template('blog/list.html', blogs=blogs, category=category)


# ----------------------------------------------------------------------
@route(bp, '/profile_blogs/<int:category>/<int:page>', '/profile_blogs/<int:category>/', methods=['GET'])
def list_profileblogs(category=0, page=1):
    """在个人中心显示自己发的blog"""
    if page == None or page <= 0:
        page = 1
    blogs = api_blog.get_latest_page_filterby(page=page, category_id=category, user=current_user)
    return render_template('blog/profile_blogs.html', blogs=blogs, category=category)


@route(bp, '/profile_auditblogs/<int:page>', methods=['GET'])
def list_auditblogs(page=1):
    """显示需要审核的文章列表"""
    blogs = api_blog.get_latest_page_filterby(page=page, can_publish=0)
    return render_template('blog/profile_auditblogs.html', blogs=blogs)


@route(bp, '/blog/audit', methods=['POST'])
def audit_blog():
    can_publish = request.json.get('can_publish', None)
    blog_id = request.json.get('blog_id', None)
    if can_publish is None or blog_id is None:
        return jsonify(dict(success=False, message=u'操作有误,不要乱搞哦'))
    blog = api_blog.get_or_404(blog_id)
    api_blog.update(blog, can_publish=can_publish)
    return jsonify(dict(success=True))


# ----------------------------------------------------------------------
@bp.route('/blog/<int:category>/<int:blog_id>', methods=['GET'])
def detail_blog(blog_id, category):
    blog = api_blog.get_or_404(blog_id)
    api_blog.update(blog, read_count=blog.read_count + 1)
    return render_template('blog/detail.html', blog=blog, category=category)


# ----------------------------------------------------------------------
@route(bp, '/', methods=['DELETE'])
# @right_require('blog')
def delete_blog():
    """Delete blog.
    :param id: blog id.
    """
    blog_id = request.json.get('blog_id', None)
    api_blog.delete(api_blog.get_or_404(blog_id))
    return jsonify(dict(success=True))
    # return redirect(url_for('.list_blog', category=category, page=1))


# ----------------------------------------------------------------------
@route(bp, '/blog/change/<int:category>/<int:blog_id>', methods=['GET', 'POST'])
# @right_require('blog')
def change_blog(blog_id, category):
    """Edit the blog.
    :param id: blog id.
    """
    blog = api_blog.get(blog_id)
    if blog.user != current_user:
        flash(gettext('This is not your blog'), category='error')
        abort(403)

    blog_form = BlogForm(obj=blog)
    if blog_form.validate_on_submit():
        flash(u'更新成功')
        api_blog.update(blog, **blog_form.data)
        return redirect(url_for('.detail_blog', blog_id=blog_id, category=category))
    if request.method == 'POST':
        flash(u'更新失败，请检查', category='danger')
    return render_template('blog/create.html', blog_form=blog_form, category=category,
                           action_url=url_for('.change_blog', blog_id=blog_id, category=category))


# ----------------------------------------------------------------------
@route(bp, '/blog/comment/<int:blog_id>', methods=['POST'])
def create_comment(blog_id):
    """Comment the blog.
    :param blog_id: The blog id to be commented.
    """
    comment_form = CommentForm()
    comment_form.csrf_enabled = False

    if comment_form.validate_on_submit():
        ref_comment_id = int(request.json.get('comment_id', 0))
        ref_comment = api_comment.get(ref_comment_id)
        floor = 1;
        first_comment = None
        if ref_comment:
            floor = ref_comment.floor + 1
            first_comment = ref_comment.first_comment or ref_comment

        com = api_comment.create(user=current_user, blog_id=blog_id, floor=floor,
                                 first_comment=first_comment,
                                 ref_comment=ref_comment, content=comment_form.content.data)
        build = []
        __build_comment(com, build)
        build.reverse()
        return jsonify(dict(success=True, comment=build))
    return jsonify(dict(sucess=False, message=comment_form.errors))


# ----------------------------------------------------------------------
@bp.route('/blog/comment/<int:blog_id>', methods=['GET'])
def list_comment(blog_id):
    """Load the comments belonge to the blog that have `:field: Comment.ref_comment` is null.
    :param blog_id: Blog id.
    :param page: Page of the comments.
    """
    page = int(request.args.get('page', 1))
    comments = api_comment.get_latest_page_filterby(page, per_page=5, blog_id=blog_id)

    ret_comms = []
    for com in comments.items:
        if com.floor and com.floor >= current_app.config['BLOG_VISIBLE_MAX_FLOOR']:
            # 达到隐藏楼层，只返回1楼和当前楼, 并指示有隐藏楼
            # 第层的结构包括,content, user, time, floor
            build = []
            build.append(__extract_comment(com.first_comment))
            build.append('more')
            build.append(__extract_comment(com))
        else:
            # 没有floor或者没有到8楼，则全部返回
            build = []
            __build_comment(com, build)
            build.reverse()
        ret_comms.append(build)

    return jsonify(dict(comments=ret_comms, totalPages=comments.pages))
    # return jsonify(dict(comments=comments.items))#, meta=dict(code=200))), 200


# ----------------------------------------------------------------------
@bp.route('blog/comment/show_more_comment/', methods=['GET'])
def show_more_comment():
    """
    """
    comment_id = request.args.get('comment_id', '', int)
    comment = api_comment.get_or_404(comment_id)
    build = []
    __build_comment(comment, build)
    build.reverse()
    return jsonify(dict(comments=build))


# ----------------------------------------------------------------------
def __extract_comment(comment):
    """Extract the wanted field.
    :param comment: :class:`dxc.blog.models.Comment` object.
    """
    return dict(id=comment.id, content=comment.content,
                user=comment.user.nickname or comment.user.email or comment.user.username,
                floor=comment.floor or 1, time=comment.create_at)


# ----------------------------------------------------------------------
def __build_comment(comment, build):
    """Build the comment floor for the give comment.
    :param comment: :class:`dxc.blog.models.Comment` object.
    :param build: Last comment floor building.
    """
    build.append(__extract_comment(comment))
    if comment.ref_comment:
        __build_comment(comment.ref_comment, build)
