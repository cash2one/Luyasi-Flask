#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from flask.ext.security import current_user
from flask_babel import gettext

from . import route
from dxc.app.models.qingbank import ContactForm
from dxc.services import api_contact, api_user, api_profile, api_sysmsg
from flaskframe.security import ProfileForm

bp = Blueprint('security-frontend', __name__, template_folder='templates', static_folder='static', url_prefix='/security')

@route(bp, '/profile/', methods=['GET'])
def index():
    #取未读消息
    # count = api_sysmsg.get_count(is_read=False)
    # print count
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
    readonly=['nickname', 'truename']#, 'college', 'major', 'clazz', 'in_college_date') #不让在macro进行自动处理
    user = api_user.get(user_id)
    
    #已经有值的才真正的设置为readonly，否则还是可以编辑的
    for pro in readonly:
        val = getattr(user.profile, pro)
        if not val and not val.strip():
            readonly.remove(pro)    

    if request.method=='GET':
        form = ProfileForm(obj=user.profile)
        return render_template('security/create_profile.html', form=form, readonly=readonly,
                                   action_url=url_for('.change_profile', user_id=user_id))
    if request.method=='POST':
        form = ProfileForm()
        
        if form.validate_on_submit():
            for pro in readonly:
                delattr(form, pro) #把不让改的属性移除。
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
    
#----------------------------------------------------------------------
@route(bp, '/sysmessages', methods=['GET'])
def list_sysmessages():
    """显示系统消息"""
    pages = api_sysmsg.get_latest_page_filterby(receiver_id=current_user.id)
    return render_template('security/profile_sysmessages.html', msgs = pages)

#----------------------------------------------------------------------
@route(bp, '/sysmessages/<int:msg_id>', methods=['GET'])
def detail_sysmessage(msg_id):
    """显示具体消息内容"""
    msg = api_sysmsg.get_or_404(msg_id)
    api_sysmsg.update(msg, is_read=True)
    return render_template('security/profile_detail_sysmessage.html', msg=msg)

#----------------------------------------------------------------------
@route(bp, '/sysmessages/delete/<int:msg_id>')
def delete_sysmessage(msg_id):
    """删除"""
    msg = api_sysmsg.get_or_404(msg_id)
    api_sysmsg.delete(msg)
    return redirect(url_for('.list_sysmessages'))
    
    