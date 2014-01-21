#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request

from flask.ext.security import current_user

from . import route
from ..services import api_contact, api_department
from ..qingbank.forms import ContactForm

bp = Blueprint('security-frontend', __name__, template_folder='templates', static_folder='static', url_prefix='/security')

@route(bp, '/profile/', methods=['GET'])
def index():
    """个人中心的主页面"""
    return render_template('security/profile.html')


@route(bp, '/profile/contact', methods=['GET'])
def profile_contact():
    """Returns the dashboard interface."""
    form = ContactForm(name=current_user.email)
    return render_template('security/profile_contact.html', form=form)

@route(bp, '/profile/security', methods=['GET'])
def profile_security():
    """Returns the dashboard interface."""
    return render_template('security/profile_security.html')    