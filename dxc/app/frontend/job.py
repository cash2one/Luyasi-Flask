# -*- coding: utf-8 -*-
"""
	Job frontend.
	~~~~~~~~~~~

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_security import current_user
from flask_babel import gettext

from . import route
from dxc.app.models.job.forms import JobForm, JobReportForm
from dxc.services import api_job, api_report

bp = Blueprint('job', __name__, template_folder='templates', static_folder='static', url_prefix='/job')

@route(bp, '/new', methods=['GET', 'POST'])
def create_job():
    form = JobForm()
    if form.validate_on_submit():
        user = None
        if current_user.get_id() is not None:
            user = current_user
        job = api_job.create(user=user, **form.data)
        return redirect(url_for('.detail_job', job_id=job.id))


    return render_template('job/create.html', form=form)

#----------------------------------------------------------------------
@bp.route('/<int:job_id>', methods=['GET'])
def detail_job(job_id):
    """"""
    job = api_job.get_or_404(job_id)
    api_job.update(job, read_count = job.read_count + 1)
    return render_template('job/detail.html', job=job)

#----------------------------------------------------------------------
@bp.route('/jobs/<int:page>', methods=['GET'])
@bp.route('/jobs/', methods=['GET'])
def list_job(page=None):
    """"""
    if page == None or page <= 0:
        page = 1
    jobs = api_job.get_latest_page_filterby(page, status=1)
    return render_template('job/list.html', jobs = jobs)


#----------------------------------------------------------------------
@bp.route('/report/<int:job_id>', methods=['GET', 'POST'])
def report_job(job_id):
    """Report a job
    """
    report_form = JobReportForm()
    if report_form.validate_on_submit():
        api_report.create(job_id=job_id, **report_form.data)
        flash(gettext(u'Thanks for your report. We will check it soon.'))
        return redirect(url_for('.list_job'))
    return render_template('job/report.html', job_id=job_id, report_form=report_form)

#----------------------------------------------------------------------
@bp.route('/reports/<int:job_id>', methods=['GET'])
def list_report(job_id):
    """"""
    job = api_job.get(job_id)
    return render_template('job/report_list.html', job=job, reports=job.reports)

@route(bp, '/profile/published_jobs/','/profile/published_jobs/<int:status>/','/profile/published_jobs/<int:status>/<int:page>', methods=['GET'])
def list_publisedjobs(status=1, page=1):
    """List jobs published by me."""
    jobs = api_job.get_latest_page_filterby(page=page, per_page=2, status=status, user_id=current_user.id)

    return render_template('job/profile_publishedjobs.html', jobs=jobs, status=status)
