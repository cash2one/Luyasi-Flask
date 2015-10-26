# -*- coding: utf-8 -*-
"""
  	Models for job.
	~~~~~~~~~~~

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from flaskframe.core import db, ModelVersion
from flaskframe.helpers import JsonSerializer

########################################################################
class Job(db.Model, ModelVersion, JsonSerializer):
    """Job model"""
    __tablename__ = 'job_job'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(5120))
    job_type = db.Column(db.Integer())
    #状态：0-审核中(可以编辑/删除)，1-审核通过(不能编辑)，2-审核不通过(可以编辑/删除，保存后为状态0)
    status = db.Column(db.Integer(), default=1, nullable=False)
    deleted = db.Column(db.Boolean(name='deleted'), default=False, nullable=False)
    #阅读次数
    read_count = db.Column(db.Integer(), default=0, nullable=False)

    # commentor
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship('User', backref=db.backref('pub_jobs', uselist=True, lazy='dynamic'))

    reports = db.relationship('Report', uselist=True, lazy='dynamic')
    
    def __repr__(self):
        return str.format('<Job: {}>', self.title)
    
    def __str__(self):
        return  u'%s' % self.title                 


########################################################################
class Report(db.Model, ModelVersion, JsonSerializer):
    """"""
    __tablename__ = 'job_report'
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(1024), nullable=False)
    job_id = db.Column(db.Integer(), db.ForeignKey('job_job.id'))
    # Only audit report can be seen
    is_audit = db.Column(db.Boolean(name='is_audit'), default=False)

    def __repr__(self):
        return str.format('<Report: {}>', self.id)
    
    def __str__(self):
        return  u'%s' % self.id             