#-*- coding:utf-8 -*-
from flask import Blueprint, request

from . import route
from ..services import api_contact, api_department
from ..core import LuyasiError, LuyasiFormError

bp_contact = Blueprint('qingbank_contact', __name__, url_prefix='/qingbank/contact')
bp_department = Blueprint('qingbank_department', __name__, url_prefix='/qingbank/department')

@route(bp_contact, '/')
def list_contacts():
	return api_contact.all()

@route(bp_contact, '/<int:id>', methods=['GET'])
def get_contact(id):
	c = api_contact.get(id)
	return dict(contact=c)

@route(bp_contact, '/<int:id>', methods=['POST'])
def update_contact(id):
	return api_contact.get(id)
