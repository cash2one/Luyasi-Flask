#-*- coding:utf-8 -*-
from flask import Blueprint, render_template, request

from . import route
from ..services import api_contact, api_department

bp = Blueprint('qingbank-frontend', __name__, template_folder='templates', static_folder='static', url_prefix='/qingbank')

@bp.route('/')
def index():
    """Returns the dashboard interface."""
    return render_template('qingbank/index.html')

@route(bp, '/contacts/<int:page>', methods=['GET'])
def list_contact_page(page):
	searchContact = request.args.get('searchContact', '').strip()
	if len(searchContact) > 0:
		page_contacts = api_contact.search(searchContact).paginate(page)
	else:
		page_contacts = api_contact.get_page(page)
	return render_template('qingbank/contact_list.html', contacts=page_contacts, searchContact=searchContact)

@route(bp, '/contact/<int:id>')
def contact_detail(id):
	contact = api_contact.get_or_404(id)
	return render_template('qingbank/contact_detail.html', contact=contact)
	