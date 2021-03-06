#-*- coding:utf-8 -*-

from flask import Blueprint, redirect, render_template, request, jsonify, flash, url_for
from flask_security import current_user
from flask_babelex import gettext

from . import route, right_require
from dxc.services import api_class, api_msg, api_apply, api_user, api_notice, api_sysmsg, api_role
from dxc.app.models.xiaoyuan import MsgForm, ReplayForm, NoticeForm
from flaskframe.security import SysMessageForm
from dxc.app.models.xiaoyuan import MessageUserAssociation, ClassUserAssociation

bp = Blueprint('xiaoyuan', __name__, template_folder='templates/xiaoyuan', static_folder='static', url_prefix='/xiaoyuan')

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
    return render_template('index.html', **__msg_info())

#----------------------------------------------------------------------
@route(bp, '/list/<int:page>', '/list/', methods=['GET'])
def list_msg(page=None):
    """"""
    if page == None or page <= 0:
        page = 1
    #查找自己的信息，且没有父消息的。
    msg_page = api_msg.get_my_msgs(current_user.id).paginate(page=1, per_page=20, error_out=True)

    return render_template('list.html', msgs=msg_page, **__msg_info())

#----------------------------------------------------------------------
@route(bp, '/detail/<int:msg_id>', methods=['GET'])
def detail_msg(msg_id):
    msg = api_msg.get(msg_id)
    msgs = []
    __build_msgs(msg, msgs)
    return render_template('detail.html', msgs=msgs)


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
        receivers = api_user.get_all(*receiver_ids)

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

    return render_template('send_msg.html', form=form)

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
    return render_template('reply_msg.html', form=form, msg_id=msg_id)



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


#----------------------------------------------------------------------
@route(bp, '/list_class', methods=['GET'])
def list_myclass():
    """列出所有的班级"""
    myclassAsscosications = current_user.class_assocs.all()
    myclasses = [assoc.clazz for assoc in myclassAsscosications]
    allclasses = [cls for cls in api_class.all() if cls not in myclasses]
    apply_ids = [apply.class_id for apply in current_user.join_applies]
    return render_template('profile_myclass.html', myclasses=myclasses, allclasses=allclasses, apply_ids=apply_ids)

#----------------------------------------------------------------------
@route(bp, '/join_class/<int:class_id>', methods=['GET'])
def apply_joinclass(class_id):
    """申请加入"""
    #如果没有填写班级的个人信息。则先提示要填写。不然不能加入。
    if current_user.profile is None:
        flash(u'你还没有填写班级个人信息，补充后才能申请加入班级')
        #form = MemberInfoForm()
        #return render_template('profile_class_memberinfo.html', form=form)
        return redirect(url_for('security-frontend.create_profile'))
    #action =1 表示加入
    apply = api_apply.create(action=1, class_id=class_id, user_id=current_user.get_id())
    return redirect(url_for('.list_myclass'))


#----------------------------------------------------------------------
@route(bp, '/list_apply/<int:page>','/list_apply', methods=['GET'])
def list_class_apply(page=1):
    """申请列表"""
    assocs = current_user.class_assocs.all()
    class_ids = [assoc.clazz.id for assoc in assocs]
    applies = api_apply.get_applies(class_ids=class_ids, page=page)
    return render_template('profile_class_apply.html', applies=applies)


#----------------------------------------------------------------------
#@route(bp, '/newmemberinfo', methods=['GET', 'POST'])
#def create_classmemberinfo():
    #"""创建自己的班级信息"""
    #form = MemberInfoForm()
    #if form.validate_on_submit():
        #u = api_meminfo.create(user=current_user, **form.data)
        #return redirect(url_for('.detail_classmemberinfo', userid=current_user.id))
    #return render_template('profile_class_memberinfo.html', form=form)

#----------------------------------------------------------------------
@route(bp, '/detailmemberinfo/<int:userid>', methods=['GET','POST'])
def detail_classmemberinfo(userid=None):
    """显示个人的班级相关信息"""
    user = api_user.get(userid)
    backurl = request.args.get('backurl')#这个是用来返回上一个页面用的
    return render_template('profile_class_memberinfo.html', meminfo=user.profile, backurl=backurl)

#----------------------------------------------------------------------
@route(bp, '/agreejoinapply/<int:applyid>', methods=['GET'])
def agree_joinapply(applyid):
    """"""
    apply = api_apply.get(applyid)
    u = api_user.get(apply.user_id)
    c = api_class.get(apply.class_id)
    assoc = ClassUserAssociation(user=u, clazz=c)
    #u.class_assocs.append(assoc)
    api_apply.delete(apply)
    return redirect(url_for('.list_class_apply', page=1))

#----------------------------------------------------------------------
@route(bp, '/rejectjoinapply', methods=['POST'])
def reject_joinapply():
    """拒绝请求"""
    form = SysMessageForm()
    form.csrf_enabled = False
    
    message = None
    applyid = request.json.get('apply_id', 0)
    apply = api_apply.get(applyid)
    if apply is None: 
        message = '申请无效'
    
    if form.validate_on_submit():
        userid = apply.user_id
        classname = apply.clazz.name
        reason = u"你的申请加入【%s】被拒绝了，理由为：【%s】" % (classname, form.content.data)
        api_sysmsg.create(receiver_id=userid, content=reason)
        api_apply.delete(apply)
        return jsonify(dict(success=True))
    
    message = u"填写不正确"
    return jsonify(dict(success=False, message=message))
        
    
    


#----------------------------------------------------------------------
@route(bp, '/newnotice/<int:class_id>', methods=['GET', 'POST'])
@right_require('xiaoyuan')
def create_notice(class_id):
    """"""
    form = NoticeForm()
    if form.validate_on_submit():
        notice = api_notice.create(user=current_user, class_id=class_id, **form.data)
        return render_template('profile_notice_detail.html', notice=notice)
    return render_template('profile_notice_create.html', form=form, class_id=class_id)

#----------------------------------------------------------------------
@route(bp, '/notices/<int:class_id>/<int:page>','/notices/<int:class_id>', methods=['GET'])
def list_notice(class_id, page=1):
    """"""
    notices = api_notice.get_latest_page_filterby(class_id=class_id)
    return render_template('profile_notice_list.html', notices=notices, class_id=class_id)

#----------------------------------------------------------------------
@route(bp, '/notice/<int:notice_id>', methods=['GET'])
def detail_notice(notice_id):
    #打开notice的时候，记录当前用户已经读了此文.同时还要为老师显示哪些人没有读这个通知。
    api_notice.readNoticeByUser(notice_id, current_user)
    notice=api_notice.get(notice_id)

    #初始化为空
    notReaders = []
    readers = []

    #所有的学生
    assocs = notice.clazz.user_assocs
    classmates = [assoc.user for assoc in assocs]
    #已经阅读的学生
    readers = notice.readers.all()
    notReaders = [ r for r in classmates if r not in readers]
    return render_template('profile_notice_detail.html', notice=notice, notReaders=notReaders, readers=readers)


#-------------------------------------------------------
# 放在页面上用的，用来检查一个用户是否为某些班级的charger
def is_charger_processor():
    """Jinja context processor for right test."""
    def is_charger():
        assocs = current_user.class_assocs.all()
        for assoc in assocs:
            if assoc.is_charger:
                return True
            
        return False
    return dict(is_charger=is_charger)