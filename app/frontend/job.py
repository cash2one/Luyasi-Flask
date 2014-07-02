# -*- coding: utf-8 -*-
"""
	Job frontend.
	~~~~~~~~~~~

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from flask import Blueprint, render_template, redirect

from . import route

from ..job.forms import JobForm
from ..services import api_job

bp = Blueprint('job', __name__, template_folder='templates', static_folder='static', url_prefix='/job')

#@route(bp, '/create', methods=['GET','POST'])
@bp.route('/create', methods=['GET', 'POST'])
def create_job():
	form = JobForm()
	if form.validate_on_submit():
		api_job.create(**form.data)
		return redirect('job/detail.html')

	return render_template('job/create.html', form=form)