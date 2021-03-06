# -*- coding: utf-8 -*-
"""
  	Models for carpool.
	~~~~~~~~~~~

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from flaskframe.core import db, ModelVersion
from flaskframe.helpers import JsonSerializer

########################################################################
class CarpoolInfo(db.Model, ModelVersion, JsonSerializer):
    """Job model"""
    __tablename__ = 'carpool_carpoolinfo'

    id = db.Column(db.Integer(), primary_key=True)

    start = db.Column(db.String(50))
    target = db.Column(db.String(50))
    route = db.Column(db.String(128))
    price = db.Column(db.Float())
    start_time = db.Column(db.DateTime(), nullable=False)
    contact_info = db.Column(db.String(128))
    #状态：0-待审核(可以编辑/删除)，1-审核通过(不能编辑)，2-审核不通过(可以编辑/删除，保存后为状态0)
    status = db.Column(db.Integer(), default=1, nullable=False)
    deleted = db.Column(db.Boolean(name='deleted'), default=False, nullable=False)

    # commentor
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship('User', backref=db.backref('carpool_infos', uselist=True, lazy='dynamic'))

    #----------------------------------------------------------------------
    def __repr__(self):
        return "<CarpoolInfo: %s - %s>" % (self.start, self.target)

    def __str__(self):
        return u" %s - %s" % (self.start, self.target)


