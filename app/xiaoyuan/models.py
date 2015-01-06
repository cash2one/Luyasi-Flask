#-*- coding: utf-8 -*-

from ..core import db, ModelVersion
from ..helpers import JsonSerializer

from ..security.models import User

academies_classes = db.Table('xiaoyuan_academies_classes',
                       db.Column('academy_id', db.Integer(), db.ForeignKey('xiaoyuan_academy.id')),
                       db.Column('class_id', db.Integer(), db.ForeignKey('xiaoyuan_class.id')))

academies_users = db.Table('xiaoyuan_academies_users',
                       db.Column('academy_id', db.Integer(), db.ForeignKey('xiaoyuan_academy.id')),
                       db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id')))

#classes_users = db.Table('xiaoyuan_classes_users',
                       #db.Column('class_id', db.Integer(), db.ForeignKey('xiaoyuan_class.id')),
                       #db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id')))

messages_users = db.Table('xiaoyuan_msges_users',
                       db.Column('messsage_id', db.Integer(), db.ForeignKey('xiaoyuan_message.id')),
                       db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id'))) 

#记录阅读情况
notices_users = db.Table('xiaoyuan_notices_users',
                       db.Column('notice_id', db.Integer(), db.ForeignKey('xiaoyuan_notice.id')),
                       db.Column('user_id', db.Integer(), db.ForeignKey('security_user.id'))) 


########################################################################
class Academy(db.Model, ModelVersion, JsonSerializer):
    __tablename__ = 'xiaoyuan_academy'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    #这个学院的人。主要是用来在领导的
    users = db.relationship(User, secondary=academies_users, backref=db.backref('academies', lazy='dynamic'))

    #----------------------------------------------------------------------
    def __repr__(self):
        return "<Academy: %s>" % self.name

    def __str__(self):
        return  u'%s' % self.name


########################################################################
class Class(db.Model, ModelVersion, JsonSerializer):
    """"""
    __tablename__ = "xiaoyuan_class"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    # 在这个班的人
    #users = db.relationship(User, secondary=classes_users, backref=db.backref('classes', lazy='dynamic'))

    # 这个班所在的学院
    academy_id = db.Column(db.Integer(), db.ForeignKey('xiaoyuan_academy.id'))
    academy = db.relationship('Academy', backref=db.backref('classes', uselist=True, lazy='dynamic'))

    #----------------------------------------------------------------------
    def __repr__(self):
        return "<Class: %s>" % self.name

    def __str__(self):
        return  u'%s' % self.name
    
    
########################################################################
class ClassUserAssociation(db.Model, JsonSerializer):
    """班级和用户的关系，加了是否为班主任的字段"""
    __tablename__ = "xiaoyuan_class_user"
    
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'), primary_key=True)
    class_id = db.Column(db.Integer(), db.ForeignKey('xiaoyuan_class.id'), primary_key=True)
    #是否为班主任
    is_charger = db.Column(db.Boolean(name='is_charger'), default=False)

    clazz = db.relationship(Class, backref=db.backref('user_assocs', lazy='dynamic'))
    user = db.relationship(User, backref=db.backref('class_assocs', lazy='dynamic'))

    def __repr__(self):
        return "<ClassUserAssociation: %s - %s>" % (self.user_id, self.class_id)

    def __str__(self):
        return  u'%s' % (str(self.user_id) + '-' + str(self.class_id))
        

class MessageUserAssociation(db.Model, JsonSerializer):
    """Middle table for message and user with extra info for reading"""
    __tablename__ = "xiaoyuan_messages_users"

    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'), primary_key=True)
    message_id = db.Column(db.Integer(), db.ForeignKey('xiaoyuan_message.id'), primary_key=True)
    is_read = db.Column(db.Boolean(name='is_read'), default=False)

    message = db.relationship('Message', backref=db.backref('user_assocs', lazy='dynamic'))
    user = db.relationship(User, backref=db.backref('message_assocs', lazy='dynamic'))

    def __repr__(self):
        return "<MessageUserAssociation: %s - %s>" % (self.user_id, self.message_id)

    def __str__(self):
        return  u'%s' % (str(self.user_id) + '-' + str(self.message_id))
    

class Message(db.Model, ModelVersion, JsonSerializer):

    __tablename__ = "xiaoyuan_message"

    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(256))

    reply_message_id = db.Column(db.Integer(), db.ForeignKey('xiaoyuan_message.id'))
    reply_message = db.relationship('Message', backref=db.backref('follow_message', uselist=False),  remote_side=[id], uselist=False)

    sender_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    sender = db.relationship('User', backref=db.backref('send_msgs', uselist=True, lazy='dynamic'),
                             foreign_keys=[sender_id])
    
    #receiver_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    #receiver = db.relationship('User', backref=db.backref('receive_msgs', uselist=True, lazy='dynamic'),
                               #foreign_keys=[receiver_id])    
    # 在这个班的人
    receivers = db.relationship(User, secondary=messages_users, backref=db.backref('messages', lazy='dynamic'))
    
    #----------------------------------------------------------------------
    def __repr__(self):
        return "<Message: %s>" % self.content

    def __str__(self):
        return  u'%s' % self.content

########################################################################
class ClassApply(db.Model, ModelVersion, JsonSerializer):
    """"""

    __tablename__ = "xiaoyuan_joinapply"
    
    id = db.Column(db.Integer(), primary_key=True)
    
    #0-表示创建，1-表示加入，2-表示删除。。。
    action = db.Column(db.Integer(), nullable=False, default=0)
    
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship(User, backref=db.backref('join_applies'))    
    
    class_id = db.Column(db.Integer(), db.ForeignKey('xiaoyuan_class.id'))
    clazz = db.relationship(Class)
    
    #可以用来发起申请的时候写原因，失败时候的原因等。
    desc = db.Column(db.String(255))
    
    #0表示申请中，1表示成功，2表示失败
    status = db.Column(db.Integer(), default=0, nullable=False)
        
    def __repr__(self):
        return "<ClassApply: %s>" % self.id

    def __str__(self):
        return  u'%s' % self.id       
    
########################################################################
#class MemberInfo(db.Model, ModelVersion, JsonSerializer):
    #"""作为班级成员需要提供的信息"""

    #__tablename__ = "xiaoyuan_memberinfo"
    #id = db.Column(db.Integer(), primary_key=True)
    
    #name = db.Column(db.String(10))
    #student_no = db.Column(db.String(15))
    #idcard = db.Column(db.String(18))
    
    #user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    #user = db.relationship(User, backref=db.backref('class_meminfo', uselist=False))   
        
    
########################################################################
class Notice(db.Model, ModelVersion, JsonSerializer):
    """发送的通知，需要记录被阅读的情况"""

    __tablename__ = "xiaoyuan_notice"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text())
    
    #发出人
    user_id = db.Column(db.Integer(), db.ForeignKey('security_user.id'))
    user = db.relationship(User, backref=db.backref('sent_notices', uselist=True, lazy='dynamic'))
    
    #发送班级
    class_id = db.Column(db.Integer(), db.ForeignKey('xiaoyuan_class.id'))
    clazz = db.relationship(Class)    
    
    #阅读人
    readers = db.relationship(User, secondary=notices_users, lazy='dynamic')
    
    def __repr__(self):
        return "<Notice: %s>" % self.id

    def __str__(self):
        return  u'%s' % self.id         
    