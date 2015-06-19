#-*- coding:utf-8 -*-
from flask import Blueprint, request,jsonify

from . import route, jsonres, paginationInfo
from ..core import LuyasiError, LuyasiFormError
from ..services import api_carpool
from flask.ext.babel import gettext

bp = Blueprint('api_carpool', __name__, url_prefix='/carpools')

#----------------------------------------------------------------------
@bp.route('/carpool-<int:carpool_id>', methods=['GET'])
def detail_carpool(carpool_id):
    """"""
    carpool = api_carpool.get(carpool_id)
    return jsonres(rv=dict(id=carpool.id,
                     price=carpool.price,
                     start=carpool.start,
                     target=carpool.target,
                     route=carpool.route,
                     publish_time=carpool.create_at))

#----------------------------------------------------------------------
@bp.route('', methods=['GET'])
def list_carpool(page=None):
    """"""
    page = int(request.args.get('page', 1));
    if page == None or page <= 0:
        page = 1
    carpools = api_carpool.get_lastest_page(page)
    pageInfo = paginationInfo(carpools)
    carpools = [dict(id=carpool.id,
                     price=carpool.price,
                     start=carpool.start,
                     target=carpool.target,
                     route=carpool.route,
                     publish_time=carpool.create_at)
                for carpool in carpools.items]
    return jsonres(rv=dict(datas=carpools, pageInfo=pageInfo))