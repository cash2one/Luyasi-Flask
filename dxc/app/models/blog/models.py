#-*- coding:utf-8 -*-

from flaskframe.core import db, ModelVersion
from flaskframe.helpers import JsonSerializer
from flaskframe.security.models import User


####################################################
class Blog(db.Model, ModelVersion, JsonSerializer):
    """Blog model"""
    __tablename__ = 'blog_blog'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text())
    # 是否可以发布，默认是可以的。只有校园通告这个的栏目，要修改默认值为不可以。需要审核才可以发布.1-可以，0-审核中, 2-不可以
    can_publish = db.Column(db.Integer(), default=1)
    #类别，blog这个模块可以放在不同的模块，由于其它功能差不多。就用一个type进行区分0-blog,1-news,2-life
    # category = db.Column(db.Integer(), default=0, nullable=False)
    #阅读次数
    read_count = db.Column(db.Integer(), default=0, nullable=False)

    # author
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship(User, backref=db.backref('blogs', uselist=True, lazy='dynamic'))
    # comments
    comments = db.relationship('Comment', lazy='dynamic', backref='blog')

    # 所属栏目
    category_id = db.Column(db.Integer(), db.ForeignKey('blog_category.id'))
    category = db.relationship('Category', backref=db.backref('blogs', uselist=True, lazy='dynamic'))

    def __repr__(self):
        return str.format('<Blog: {}>', self.title)
    
    def __str__(self):
        return  u'%s' % self.title             

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
    first_comment = db.relationship('Comment', foreign_keys=[first_comment_id], remote_side=[id])

    blog_id = db.Column(db.Integer, db.ForeignKey('blog_blog.id'))

    # commentor
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship('User', backref=db.backref('comments', uselist=True, lazy='dynamic'))
    
    # ref comment
    ref_comment_id = db.Column(db.Integer(), db.ForeignKey('blog_comment.id'))
    ref_comment = db.relationship('Comment', foreign_keys=[ref_comment_id], remote_side=[id])

    def __repr__(self):
        return str.format('<Comment: {}>', self.id)
    
    def __str__(self):
        return  u'%s' % self.id

class Category(db.Model, ModelVersion, JsonSerializer):
    """栏目类别
    """
    __tablename__ = 'blog_category'

    id = db.Column(db.Integer(), primary_key=True)
    # id = db.Column(GUID(), primary_key=True, default=uuid.uuid4())
    name = db.Column(db.String(50))
    order = db.Column(db.Integer(), default=0)
    parent_id = db.Column(db.Integer(), db.ForeignKey('blog_category.id'))
    parent = db.relationship('Category', remote_side=[id], backref='children')

    def __repr__(self):
        return str.format('<Category: {}>', self.name)

    def __str__(self):
        return  u'%s' % self.name