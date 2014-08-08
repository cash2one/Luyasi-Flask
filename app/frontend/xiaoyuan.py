#-*- coding:utf-8 -*-

from flask import Blueprint, redirect, render_template, request, jsonify, flash, url_for
from flask_security import current_user
from flask_babelex import gettext

from . import route
from ..core import db

from ..services import api_academy, api_class, api_msg, api_user
from ..xiaoyuan.forms import MsgForm, ReplayForm
from ..xiaoyuan.models import MessageUserAssociation, Message

bp = Blueprint('xiaoyuan', __name__, template_folder='templates', static_folder='static', url_prefix='/xiaoyuan')

#----------------------------------------------------------------------
def __msg_info():
    """message的统计信息"""
    msg_cnt = current_user.message_assocs.count()
    unread_cnt = current_user.message_assocs.filter_by(is_read=False).count()
    return {'msg_cnt':msg_cnt, 'unread_cnt':unread_cnt}

#----------------------------------------------------------------------
@route(bp, '/index')
def index():
    """根据不同的角色会看到不同的主页内容"""
    return render_template('xiaoyuan/index.html', **__msg_info())

#----------------------------------------------------------------------
@route(bp, '/list/<int:page>', '/list/', methods=['GET'])
def list_msg(page=None):
    """"""
    if page == None or page <= 0:
        page = 1
    #查找自己的信息，且没有父消息的。
    msg_page = api_msg.get_my_msgs(current_user.id).paginate(page=1, per_page=20, error_out=True)

    return render_template('xiaoyuan/list.html', msgs=msg_page, **__msg_info())

#----------------------------------------------------------------------
@route(bp, '/detail/<int:msg_id>', methods=['GET'])
def detail_msg(msg_id):
    msg = api_msg.get(msg_id)
    msgs = []
    __build_msgs(msg, msgs)
    return render_template('xiaoyuan/detail.html', msgs=msgs)


def __build_msgs(msg, build):
    build.append(msg)
    if msg.follow_message:
        __build_msgs(msg.follow_message, build)

#----------------------------------------------------------------------
@route(bp, '/send_msg', methods=['GET', 'POST'])
def send_msg():
    """发送指定的消息"""
    form = MsgForm()
    #form.receivers.choices = [(u.id, u.email) for u in api_user.all()]
    if form.validate_on_submit():
        receiver_ids = form.receivers.data
        content = form.content.data

        # 没有id的
        msg = api_msg.new(content=content, sender=current_user)
        receivers = api_user.get_all(*receiver_ids)

        for rec in receivers:
            association = MessageUserAssociation()
            association.message = msg
            association.user = rec
            rec.message_assocs.append(association)

        flash(gettext(u'Message is sent'))
        return redirect(url_for('.index'))

    return render_template('xiaoyuan/send_msg.html', form=form)

#----------------------------------------------------------------------
@route(bp, '/<int:msg_id>/reply', methods=['GET','POST'])
def reply_msg(msg_id=None):
    """"""
    form = ReplayForm()
    if form.validate_on_submit():
        reply_msg = api_msg.get(msg_id)
        api_msg.create(content=form.content.data, sender=current_user, reply_msg=reply_msg)
        flash(gettext(u'Message is sent'))
        return redirect(url_for('.index'))
    return render_template('xiaoyuan/reply_msg.html', form=form, msg_id=msg_id)



@route(bp, '/list_receivers', methods=['GET'])
def list_receivers():
    """List receivers that only have rights to see."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)

    classes = current_user.classes

    users = api_user.get_user_from_classes(class_ids=[cls.id for cls in classes])
    #需要把users<pagenate对象>的相关属性提出来
    userdict = [{'id': u.id, 'text': str(u)} for u in users.items]
    return jsonify(dict(data=userdict,
                        pageinfo=dict(has_next=users.has_next, has_prev=users.has_prev,
                                      next_num=users.next_num, pages=users.pages,
                                      per_page=users.per_page, prev_num=users.prev_num,
                                      total=users.total)))