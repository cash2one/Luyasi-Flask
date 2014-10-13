#-*- coding:utf-8 -*-
from flask import Blueprint, request,jsonify

from . import route, jsonres
from ..core import LuyasiError, LuyasiFormError
from ..services import api_carpool
from flask.ext.babel import gettext

bp = Blueprint('carpool', __name__, url_prefix='/carpool')

#----------------------------------------------------------------------
@bp.route('/<int:carinfo_id>', methods=['GET'])
def detail_carinfo(carinfo_id):
	""""""
	carinfo = api_carpool.get(carinfo_id)
	return jsonres(carinfo, 200)

#----------------------------------------------------------------------
@bp.route('/carinfos/<int:page>', methods=['GET'])
@bp.route('/carinfos/', methods=['GET'])
def list_carinfo(page=None):
	""""""
	if page == None or page <= 0:
		page = 1
	carinfos = api_carpool.get_lastest_page(page)
	carinfos = [dict(price=carinfo.price, 
	                 start=carinfo.start,
	                 target=carinfo.target,
	                 user=dict(username=carinfo.user.username or carinfo.user.email,
	                      userid=carinfo.user.id)
	                 ) 
	            for carinfo in carinfos.items]
	return jsonres(carinfos, 200)