#-*- coding:utf-8 -*-
from flask import Blueprint, render_template

from . import route
from ..services import api_job, api_carpool, api_blog

bp = Blueprint('frontend-index', __name__,    template_folder='templates', static_folder='static')

#----------------------------------------------------------------------
@bp.route('/')
def index():
	""""""
	jobs = api_job.get_lastest_page(1, per_page=5)
	carinfos = api_carpool.get_lastest_page(1, per_page=5)
	blogs = api_blog.get_lastest_page(1, per_page=5)
	return render_template('index/index.html', jobs=jobs, carinfos=carinfos, blogs=blogs)

#----------------------------------------------------------------------
@bp.route('/test')
def test_form():
	"""Return form"""
	return render_template('testform.html')