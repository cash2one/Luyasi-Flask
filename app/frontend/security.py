#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
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

@route(bp, '/search_user')
def search_user():
    per_page = request.args.get('per_page', None, type=int)
    term = request.args.get('term', None)
    page = request.args.get('page', 1, type=int)
    # users = api_user.get_page_filterby(page=page, per_page=per_page or 20, email=term)
    users = api_user.all()
    return jsonify(dict(total=20, results=[{'id': u.id, 'text': u.email} for u in users]))

@route(bp, '/list_user', methods=['GET'])
def list_user():
    page = request.args.get('page', 1, type=int)
    users = api_user.get_page(page, per_page=3)
    #需要把users<pagenate对象>的相关属性提出来
    userdict = [{'id': u.id, 'text': str(u)} for u in users.items]
    return jsonify(dict(data=userdict,
                        pageinfo=dict(has_next=users.has_next, has_prev=users.has_prev,
                                      next_num=users.next_num, pages=users.pages, per_page=users.per_page, prev_num=users.prev_num,
                                      total=users.total)))