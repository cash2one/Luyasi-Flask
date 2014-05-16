#-*- coding:utf-8 -*-
from ..core import db
from ..helpers import JsonSerializer

####################################################
class Blog(db.Model, JsonSerializer):
    """Blog model"""
    __tablename__ = 'blog_blog'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), unique=True)
    content = db.Column(db.Text())
    
    # author
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship('User', backref=db.backref('blogs', uselist=True, lazy='dynamic'))    
    # comments
    comments = db.relationship('Comment', lazy='dynamic', backref='blog')

    def __repr__(self):
        return str.format('<Blog {}>', self.title)
    
####################################################
class Comment(db.Model, JsonSerializer):
    """Comments for blog"""
    
    __tablename__ = 'blog_comment'
    
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(1024))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog_blog.id'))
    
    # commentor
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship('User', backref=db.backref('blogs', uselist=True, lazy='dynamic'))      
    # ref comment
    ref_comment_id = db.Column(db.Integer(), db.ForeignKey('blog_comment.id'))
    ref_comment = db.relationship('Comment', remote_side=[id], backref='children')    