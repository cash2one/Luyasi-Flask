#-*- coding:utf-8 -*-
from ..core import db, ModelVersion
from ..helpers import JsonSerializer
from ..security.models import User

####################################################
class Blog(db.Model, ModelVersion, JsonSerializer):
    """Blog model"""
    __tablename__ = 'blog_blog'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), unique=True)
    content = db.Column(db.Text())

    # author
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship(User, backref=db.backref('blogs', uselist=True, lazy='dynamic'))
    # comments
    comments = db.relationship('Comment', lazy='dynamic', backref='blog')

    #: Optimistic locking
    version = db.Column(db.Integer(), nullable=False)
    __mapper_args__ = {
        "version_id_col": version
    }

    def __repr__(self):
        return str.format('<Blog: {}>', self.title)

####################################################
class Comment(db.Model, ModelVersion, JsonSerializer):
    """Comments for blog"""

    __tablename__ = 'blog_comment'
    # 这两个是来自于backref
    __json_hidden__ = ['blog', 'ref_comment']
    #__json_depth_no_limit__ = ['children']

    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(1024))
    # 第几楼
    floor = db.Column(db.Integer())
    # 用来记住第一楼用的
    first_comment_id = db.Column(db.Integer(), db.ForeignKey('blog_comment.id'))
    first_comment = db.relationship('Comment', remote_side=[id], foreign_keys=[first_comment_id])

    blog_id = db.Column(db.Integer, db.ForeignKey('blog_blog.id'))

    # commentor
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship('User', backref=db.backref('comments', uselist=True, lazy='dynamic'))
    # ref comment
    ref_comment_id = db.Column(db.Integer(), db.ForeignKey('blog_comment.id'))
    ref_comment = db.relationship('Comment', remote_side=[id], foreign_keys=[ref_comment_id])

    #: Optimistic locking
    version = db.Column(db.Integer(), nullable=False)
    __mapper_args__ = {
        "version_id_col": version
    }

    def __repr__(self):
        return str.format('<Comment: {}>', self.id)