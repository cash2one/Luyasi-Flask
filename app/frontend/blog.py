#-*- coding:utf-8 -*-
import re
from functools import partial

from flask import current_app, abort, flash, session
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import current_user
from flask_principal import Permission, Need
from flask_babel import gettext

from . import route, right_require
from ..core import RightNeed
from ..services import api_blog, api_comment
from ..blog.forms import BlogForm, CommentForm
from ..framework.captcha import make_simple_captcha

bp = Blueprint('blog', __name__, template_folder='templates', static_folder='static', url_prefix='/blog')

#--------------------------------------------------------
@route(bp, '/new', methods=['GET', 'POST'])
@right_require('blog')
def create_blog():
	blog_form = BlogForm()
	if blog_form.validate_on_submit():
		blog_id = blog_form.id.data
		if blog_id == 0:
			blog = api_blog.create(user=current_user, **blog_form.data)
		else:
			api_blog.update(api_blog.get(blog_id), **blog_form.data)
		return redirect(url_for('.list_blog'))
	return render_template('blog/create.html', blog_form=blog_form)

#--------------------------------------------------------
#@route(bp, '/blogs/<int:page>', '/blogs/')
@bp.route('/blogs/<int:page>', methods=['GET'])
@bp.route('/blogs/', methods=['GET'])
def list_blog(page=None):
	if page == None or page <= 0:
		page = 1
	blogs = api_blog.get_lastest_page(page)
	return render_template('blog/list.html', blogs = blogs, test="<p>test</p>")

#----------------------------------------------------------------------
@bp.route('/blog/<int:blog_id>', methods=['GET'])
def detail_blog(blog_id):
	blog = api_blog.get(blog_id)
	return render_template('blog/detail.html', blog=blog)

#----------------------------------------------------------------------
@route(bp, '/blog/delete/<int:blog_id>')
@right_require('blog')
def delete_blog(blog_id):
	"""Delete blog.
	:param id: blog id.
	"""
	api_blog.delete(api_blog.get_or_404(blog_id))
	return redirect(url_for('.list'))

#----------------------------------------------------------------------
@route(bp, '/blog/change/<int:blog_id>')
@right_require('blog')
def change_blog(blog_id):
	"""Edit the blog.
	:param id: blog id.
	"""
	blog = api_blog.get(blog_id)
	if blog.user != current_user:
		flash(gettext('This is not your blog'), category='error')
		abort(403)
	blog_form = BlogForm(obj=blog)
	return render_template('blog/create.html', blog_form=blog_form)

#----------------------------------------------------------------------
@route(bp, '/blog/comment/<int:blog_id>', methods=['POST'])
def create_comment(blog_id):
	"""Comment the blog.
	:param blog_id: The blog id to be commented.
	"""
	comment_form =CommentForm()
	comment_form.csrf_enabled = False

	if comment_form.validate_on_submit():
		ref_comment_id = int(request.json.get('comment_id', 0))
		ref_comment = api_comment.get(ref_comment_id)
		floor = 1;
		first_comment = None
		if ref_comment:
			floor = ref_comment.floor + 1
			first_comment = ref_comment.first_comment or ref_comment

		com = api_comment.create(user=current_user, blog_id=blog_id, floor = floor,
		                        first_comment = first_comment,
		                        ref_comment_id=ref_comment_id or None, content=comment_form.content.data)
		build = []
		__build_comment(com, build)
		build.reverse()
		return jsonify(dict(success=True, comment=build))
	return jsonify(dict(sucess=False, message=comment_form.errors))

#----------------------------------------------------------------------
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
	#return jsonify(dict(comments=comments.items))#, meta=dict(code=200))), 200

#----------------------------------------------------------------------
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


#----------------------------------------------------------------------
def __extract_comment(comment):
	"""Extract the wanted field.
	:param comment: :class:`app.blog.models.Comment` object.
	"""
	return dict(id=comment.id, content=comment.content, user=comment.user.nickname or comment.user.email or comment.user.username,
	            floor=comment.floor or 1, time = comment.create_at)

#----------------------------------------------------------------------
def __build_comment(comment, build):
	"""Build the comment floor for the give comment.
	:param comment: :class:`app.blog.models.Comment` object.
	:param build: Last comment floor building.
	"""
	build.append(__extract_comment(comment))
	if comment.ref_comment:
		__build_comment(comment.ref_comment, build)
