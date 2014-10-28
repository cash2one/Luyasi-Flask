#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from flask.ext.security import current_user
from wtforms.ext.sqlalchemy.orm import model_form
from flask_babel import gettext

from . import route
from ..qingbank.forms import ContactForm
from ..services import api_contact, api_department, api_user, api_role, api_job

bp = Blueprint('security-frontend', __name__, template_folder='templates', static_folder='static', url_prefix='/security')

@route(bp, '/profile/', methods=['GET'])
def index():
    """Rerturn personal profile page."""
    return render_template('security/profile.html')


@route(bp, '/profile/contact', methods=['GET', 'POST'])
def profile_contact():
    """Contact of personal profile."""
    if current_user.contact:
        form = ContactForm(request.form,  obj=current_user.contact)
    else:
        if request.method == 'GET':
            flash(gettext('Maybe you can show more of yourself'))
        form = ContactForm(request.form)

    if form.validate_on_submit():
        if current_user.contact:
            # form.populate_obj(current_user.contact)这是把值 放到model的方法
            form.populate_obj(current_user.contact)
            api_contact.update(current_user.contact)
            flash(gettext('Update personal info success'))
        else:
            contact = api_contact.new()
            form.populate_obj(contact)
            contact.user = current_user
            contact = api_contact.save(contact)
            flash(gettext('Add personal info success'))
    #    return redirect(url_for('.profile_contact'))
    return render_template('security/profile_contact.html', form=form)

@route(bp, '/profile/security', methods=['GET'])
def profile_security():
    """Change personal profile password."""
    return render_template('security/profile_security.html')

@route(bp, '/profile/published_jobs/','/profile/published_jobs/<int:status>/','/profile/published_jobs/<int:status>/<int:page>', methods=['GET'])
def list_publisedjobs(status=1, page=1):
    """List jobs published by me."""
    jobs = api_job.get_latest_page_filterby(page=page, per_page=2, status=status)
    return render_template('security/profile_publishedjobs.html', jobs=jobs, status=status)

@route(bp, '/search_user')
def search_user():
    per_page = request.args.get('per_page', None, type=int)
    term = request.args.get('term', None)
    page = request.args.get('page', 1, type=int)

    paginate = api_user.search_user(term).paginate(page, per_page)
    users = paginate.items
    total = paginate.total
    return jsonify(dict(total=total, results=[{'id': u.id, 'text': u.contact.name} for u in users]))
