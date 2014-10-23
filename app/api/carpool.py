#-*- coding:utf-8 -*-
from flask import Blueprint, request,jsonify

from . import route, jsonres, paginationInfo
from ..core import LuyasiError, LuyasiFormError
from ..services import api_carpool
from flask.ext.babel import gettext

bp = Blueprint('carpool', __name__, url_prefix='/carpool')

#----------------------------------------------------------------------
@bp.route('/<int:carinfo_id>', methods=['GET'])
def detail_carinfo(carinfo_id):
	""""""
	carinfo = api_carpool.get(carinfo_id)
	return jsonres(rv=carinfo)

#----------------------------------------------------------------------
@bp.route('/carinfos/<int:page>', methods=['GET', 'POST'])
@bp.route('/carinfos/', methods=['GET', 'POST'])
def list_carinfo(page=None):
	""""""
	if page == None or page <= 0:
		page = 1
	carinfos = api_carpool.get_lastest_page(page)
	pageInfo = paginationInfo(carinfos)
	carinfos = [dict(id=carinfo.id,
	                 price=carinfo.price, 
	                 start=carinfo.start,
	                 target=carinfo.target,
	                 route=carinfo.route,
	                 publish_time=carinfo.create_at)
	            for carinfo in carinfos.items]
	return jsonres(rv=dict(carInfos=carinfos, pageInfo=pageInfo))