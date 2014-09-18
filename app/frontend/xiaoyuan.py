#-*- coding:utf-8 -*-

from flask import Blueprint, redirect, render_template, request, jsonify
from flask_security import current_user

from . import route

from ..services import api_academy, api_class, api_msg, api_user, api_role
from ..xiaoyuan.forms import MsgForm

bp = Blueprint('xiaoyuan', __name__, template_folder='templates', static_folder='static', url_prefix='/xiaoyuan')

#----------------------------------------------------------------------
@route(bp, '/index')
def index():
    """根据不同的角色会看到不同的主页内容"""
    return render_template('xiaoyuan/index.html')

#----------------------------------------------------------------------
@route(bp, '/send_msg', methods=['GET', 'POST'])
def send_msg():
    """发送指定的消息"""
    form = MsgForm()
    #form.receivers.choices = [(u.id, u.email) for u in api_user.all()]
    if form.validate_on_submit():
        receiver_ids = form.receivers.data
        receivers = api_user.get_all(*receiver_ids)
        
        pass
    return render_template('xiaoyuan/send_msg.html', form=form)


@route(bp, '/list_receivers', methods=['GET'])
def list_receivers():
    """List receivers that only have rights to see."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)

    classes = current_user.classes
    role_ids = []
    if current_user.has_role(u'辅导员'):
        # 如果当前的角色是辅导员，则可以看到所有的本班的人，除了自己。
        student_role = api_role.first(name=u'学生')
        role_ids = [student_role.id]
    elif current_user.has_role(u'学生'):
        # 如果当前的角色是学生，则只可以看到学生以外的角色
        teacher_role = api_role.first(name=u'辅导员')
        role_ids = [teacher_role.id]
    
    users = api_user.get_user_from_classes(class_ids=[cls.id for cls in classes], role_ids=role_ids)
    #需要把users<pagenate对象>的相关属性提出来
    userdict = [{'id': u.id, 'text': str(u)} for u in users.items]
    return jsonify(dict(data=userdict,
                        pageinfo=dict(has_next=users.has_next, has_prev=users.has_prev,
                                      next_num=users.next_num, pages=users.pages,
                                      per_page=users.per_page, prev_num=users.prev_num,
                                      total=users.total)))