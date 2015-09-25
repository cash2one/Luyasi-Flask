#-*- coding:utf-8 -*-
from flask import Blueprint, jsonify

from . import route
from dxc.services import api_contact

bp_contact = Blueprint('qingbank_contact', __name__, url_prefix='/qingbank/contact')
bp_department = Blueprint('qingbank_department', __name__, url_prefix='/qingbank/department')

@route(bp_contact, '/')
def list_contacts():
    return jsonify(api_contact.all())

@route(bp_contact, '/<int:id>', methods=['GET'])
def get_contact(id):
    c = api_contact.get(id)
    return jsonify(dict(contact=c))

@route(bp_contact, '/<int:id>', methods=['POST'])
def update_contact(id):
    return api_contact.get(id)

@bp_contact.route('/test')
def kk():
    """"""
    return jsonify(dict(user='kinorsi'))

@bp_contact.route('/testlist')
def list():
    """"""
    return jsonify(dict(followerList=[dict(user='luyasi'),dict(user='kk')]))

@bp_contact.route('/testlist2')
def list2():
    """"""
    import json
    return json.dumps([{'user':'kinorsi'}, {'user':'luyasi'}])
    #return jsonify({'name':'kk', 'list':[{'age':10},{'age':20}]})


@bp_contact.route('/joblist')
def joblist():
    """"""
    import json
    jobs = []
    for i in range(1,100):
        jobs.append({'title': 'job ' + str(i)})

    return json.dumps(jobs)
    #return jsonify({'name':'kk', 'list':[{'age':10},{'age':20}]})