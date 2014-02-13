#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from flask.ext.security import current_user
from wtforms.ext.sqlalchemy.orm import model_form

from . import route
from ..qingbank.forms import ContactForm, CF
from ..services import api_contact, api_department, api_user, api_role

bp = Blueprint('security-frontend', __name__, template_folder='templates', static_folder='static', url_prefix='/security')

@route(bp, '/profile/', methods=['GET'])
def index():
    """个人中心的主页面"""
    return render_template('security/profile.html')


@route(bp, '/profile/contact', methods=['GET', 'POST'])
def profile_contact():
    """联系信息"""
    form = CF(request.form,  obj=current_user.contact)
    # form.populate_obj(current_user.contact)这是把值 放到model的方法
    
    if form.validate_on_submit():
        form.populate_obj(current_user.contact)
        api_contact.save(current_user.contact)
        return redirect(url_for('.profile_contact'))
    return render_template('security/profile_contact.html', form=form)

@route(bp, '/profile/security', methods=['GET'])
def profile_security():
    """修改密码"""
    return render_template('security/profile_security.html')    
