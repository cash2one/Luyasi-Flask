#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request

from . import route
from dxc.services import api_contact, api_department
from flask.ext.principal import Permission, RoleNeed
# from ..core import mail
# from flask.ext.mail import Message

bp = Blueprint('qingbank-frontend', __name__,    template_folder='templates', static_folder='static', url_prefix='/qingbank')

# admin_permission = Permission(RoleNeed('admin'))


@bp.route('/')
# @admin_permission.require()
def index():
    """Returns the qingbank index page."""
    return render_template('qingbank/index.html')

#@bp.route('/contacts/<int:page>', methods=['GET'])
@route(bp, '/contacts/<int:page>', methods=['GET'])
def list_contact_page(page):
    """Return one page contacts.

    :param page: current page need to be return. page >= 1.
    """

    searchContact = request.args.get('searchContact', '').strip()
    if len(searchContact) > 0:
        page_contacts = api_contact.search(searchContact).paginate(page)
    else:
        page_contacts = api_contact.get_page(page)
    return render_template('qingbank/contact_list.html', contacts=page_contacts, searchContact=searchContact)

@bp.route('/contact/<int:id>', methods=['GET'])
def contact_detail(id):
    """Return detail contact for the given id.

    :param id: contact id.
    """
    contact = api_contact.get_or_404(id)
    return render_template('qingbank/contact_detail.html', contact=contact)

# @bp.route('/sendmail', methods=['GET'])
# def send_mail():
# 	msg = Message('a subject', recipients=['172440249@qq.com'])
# 	msg.body='text body'
# 	msg.html = '<h1>h1</h1> Html test'
# 	mail.send(msg)
# 	return 'OK'