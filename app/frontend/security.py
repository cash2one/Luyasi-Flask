#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from flask.ext.security import current_user
from wtforms.ext.sqlalchemy.orm import model_form
from flask_babel import gettext

from . import route
from ..qingbank.forms import ContactForm
from ..services import api_contact, api_department, api_user, api_role, api_job, api_profile
from ..security.forms import ProfileForm

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

@route(bp, '/search_user')
def search_user():
    per_page = request.args.get('per_page', None, type=int)
    term = request.args.get('term', None)
    page = request.args.get('page', 1, type=int)

    paginate = api_user.search_user(term).paginate(page, per_page)
    users = paginate.items
    total = paginate.total
    return jsonify(dict(total=total, results=[{'id': u.id, 'text': u.contact.name} for u in users]))

#----------------------------------------------------------------------
@route(bp, '/myprofile/create', methods=['GET', 'POST'])
def create_profile():
    """"""
    form = ProfileForm()
    if form.validate_on_submit():
        if api_profile.exist(nickname=form.nickname.data):
            flash(u'昵称已经被别人用了', category='danger')
            return render_template('security/create_profile.html', form=form,
                           action_url=url_for('.create_profile'))
        
        profile = api_profile.create(user_id=current_user.id, **form.data)
        return redirect(url_for('.detail_profile', user_id=current_user.id))
    if request.method=='POST':
        flash(u'更新失败，请检查', category='danger')
    return render_template('security/create_profile.html', form=form,
                           action_url=url_for('.create_profile'))

@route(bp, '/myprofile/change/<int:user_id>', methods=['GET', 'POST'])
def change_profile(user_id):
    readonly=('nickname',) #不让在macro进行自动处理
    if request.method=='GET':
        user = api_user.get(user_id)
        form = ProfileForm(obj=user.profile)
        return render_template('security/create_profile.html', form=form, readonly=readonly,
                                   action_url=url_for('.change_profile', user_id=user_id))
    if request.method=='POST':
        form = ProfileForm()
        if form.validate_on_submit():
            del form.nickname #不让改nickname
            profile = api_profile.get(form.id.data)
            api_profile.update(profile, **form.data)
            flash(u'更新个人信息成功')
            return redirect(url_for('.detail_profile', user_id=current_user.id))
        else:
            flash(u'更新失败，请检查内容', category='danger')
            return render_template('security/create_profile.html', form=form,
                           action_url=url_for('.change_profile', user_id=user_id))

@route(bp, '/myprofile/detail/<int:user_id>', methods=['GET', 'POST'])
def detail_profile(user_id):
    user = api_user.get(user_id)
    if user.profile:
        form = ProfileForm(obj=user.profile)
        return render_template('security/detail_profile.html', form=form,
                               action_url=url_for('.change_profile', user_id=current_user.id))
    else:
        flash(u'你还没有填写个人信息，补充信息有惊喜哦')
        return redirect(url_for('.create_profile'))