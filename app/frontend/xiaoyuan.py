#-*- coding:utf-8 -*-

from flask import Blueprint, redirect, render_template

from . import route

from ..services import api_academy, api_class, api_msg, api_user
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
    form.receivers.choices = [(u.id, u.email) for u in api_user.all()]
    return render_template('xiaoyuan/send_msg.html', form=form)
