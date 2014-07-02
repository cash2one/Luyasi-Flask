# -*- coding: utf-8 -*-
"""
  	Models for job.
	~~~~~~~~~~~

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from ..core import db, ModelVersion
from ..helpers import JsonSerializer

########################################################################
class Job(db.Model, ModelVersion, JsonSerializer):
	"""Job model"""
	__tablename__ = 'job_job'
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(80))
	content = db.Column(db.String(5120))
	job_type = db.Column(db.Integer())

	# commentor
	user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
	user = db.relationship('User', backref=db.backref('pub_jobs', uselist=True, lazy='dynamic'))
