#-*- coding:utf-8 -*-

import time

from flask import Blueprint, request,jsonify
from flask.ext.babel import gettext

from . import route, jsonres
from ..core import LuyasiError, LuyasiFormError
from ..services import api_job
from ..helpers import mkmillseconds
from . import paginationInfo, jsonres



bp = Blueprint('api_job', __name__, url_prefix='/jobs')

#----------------------------------------------------------------------
@bp.route('/job-<int:job_id>', methods=['GET'])
def detail_job(job_id):
    """"""
    job = api_job.get(job_id)
    return jsonres(rv=dict(id=job.id,
                           title=job.title,
                           readCount=job.read_count,
                           status=job.status,
                           content=job.content,
                           userId=job.user_id,
                           type=job.job_type,
                           create_at=mkmillseconds(job.create_at)))

#----------------------------------------------------------------------
@bp.route('', methods=['GET'])
def list_job(page=None):
    """"""
    page = int(request.args.get('page', 1))
    if page == None or page <= 0:
        page = 1
    jobs = api_job.get_lastest_page(page)
    pageInfo = paginationInfo(jobs)
    jobs = [dict(id=job.id,
                 title=job.title,
                 type=job.job_type,
                 create_at=mkmillseconds(job.create_at)) for job in jobs.items]
    return jsonres(rv=dict(datas=jobs, pageInfo=pageInfo))