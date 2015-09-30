#-*- coding:utf-8 -*-
from flask import Blueprint, request,jsonify

from . import route, jsonres
from ..core import LuyasiError, LuyasiFormError
from ..services import api_job
from flask.ext.babel import gettext

bp = Blueprint('job', __name__, url_prefix='/job')

#----------------------------------------------------------------------
@bp.route('/<int:job_id>', methods=['GET'])
def detail_job(job_id):
	""""""
	job = api_job.get(job_id)
	return jsonres(job, 200)

#----------------------------------------------------------------------
@bp.route('/jobs/<int:page>', methods=['GET'])
@bp.route('/jobs/', methods=['GET'])
def list_job(page=None):
	""""""
	if page == None or page <= 0:
		page = 1
	jobs = api_job.get_lastest_page(page)
	jobs = [job for job in jobs.items]
	return jsonres(jobs, 200)