#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from flask.ext.security import current_user
from wtforms.ext.sqlalchemy.orm import model_form

from . import route
from ..qingbank.forms import ContactForm
from ..services import api_contact, api_department, api_user, api_role

bp = Blueprint('security-frontend', __name__, template_folder='templates', static_folder='static', url_prefix='/security')

@route(bp, '/profile/', methods=['GET'])
def index():
    """Rerturn personal profile page."""
    return render_template('security/profile.html')


@route(bp, '/profile/contact', methods=['GET', 'POST'])
def profile_contact():
    """Contact of personal profile."""
    if current_user.contact.count() >=1:
        form = ContactForm(request.form,  obj=current_user.contact[0])
    else:
        form = ContactForm(request.form)
    # form.populate_obj(current_user.contact)这是把值 放到model的方法
    
    if form.validate_on_submit():
        if current_user.contact.count() >= 1:
            form.populate_obj(current_user.contact.first())
            api_contact.update(current_user.contact.first())
        else:
            contact = api_contact.new()
            form.populate_obj(contact)
            contact.user = current_user
            contact = api_contact.save(contact)
        return redirect(url_for('.profile_contact'))
    return render_template('security/profile_contact.html', form=form)

@route(bp, '/profile/security', methods=['GET'])
def profile_security():
    """Change personal profile password."""
    return render_template('security/profile_security.html')    
