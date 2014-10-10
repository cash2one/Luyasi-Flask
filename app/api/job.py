#-*- coding:utf-8 -*-
from flask import Blueprint, request,jsonify

from . import route
from ..core import LuyasiError, LuyasiFormError
from ..services import api_job
from flask.ext.babel import gettext

bp = Blueprint('job', __name__, url_prefix='/job')

#----------------------------------------------------------------------
@bp.route('/<int:job_id>', methods=['GET'])
def detail_job(job_id):
	""""""
	job = api_job.get_or_404(job_id)
	return render_template('job/detail.html', job=job)

#----------------------------------------------------------------------
@bp.route('/jobs/<int:page>', methods=['GET'])
@bp.route('/jobs/', methods=['GET'])
def list_job(page=None):
	""""""
	if page == None or page <= 0:
		page = 1
	jobs = api_job.get_lastest_page(page)
	return render_template('job/list.html', jobs = jobs)