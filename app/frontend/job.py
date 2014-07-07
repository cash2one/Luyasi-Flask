# -*- coding: utf-8 -*-
"""
	Job frontend.
	~~~~~~~~~~~

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_security import current_user, AnonymousUser
from flask_babel import gettext

from . import route
from ..job.forms import JobForm, JobReportForm
from ..services import api_job, api_report

bp = Blueprint('job', __name__, template_folder='templates', static_folder='static', url_prefix='/job')

@bp.route('/create', methods=['GET', 'POST'])
def create_job():
	form = JobForm()
	if form.validate_on_submit():
		user = None
		if current_user.get_id() is not None:
			user = current_user
		job = api_job.create(user=user, **form.data)
		print job.id
		return redirect('/job/' + str(job.id))

	return render_template('job/create.html', form=form)

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


