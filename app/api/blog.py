# -*- coding: utf-8 -*-
"""
   $(filename)
    ~~~~~~~~~~~

    Blog api

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from flask import Blueprint, jsonify, request
from . import route

bp = Blueprint('api_blog', __name__, url_prefix='/blog')

#----------------------------------------------------------------------
@bp.route('/create', methods=['POST', 'GET'])
def create_blog():
    """"""
    if request.method == 'GET':
        return jsonify(dict(method='GET'))
    else:
        return jsonify(dict(method='POST'))
