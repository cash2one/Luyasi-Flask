# -*- coding:utf-8 -*-

from flask import Blueprint, request
from flask_security import current_user

from flaskframe.helpers import mkmillseconds
from thld.services import apiGarageRent
from thld.app.models.garage.forms import GarageForm
from . import paginationInfo, jsonres, route

bp = Blueprint('apiGarage', __name__, url_prefix='/garages')


@bp.route('', methods=['GET'])
def list_garage():
    page = int(request.args.get('page', 1))
    garages = apiGarageRent.get_lastest_page(page)
    page_info = paginationInfo(garages)
    carpools = [_garage_json(garage) for garage in garages.items]
    return jsonres(rv=dict(datas=carpools, pageInfo=page_info))


@route(bp, 'garage-new', methods=['POST'])
def create_garage():
    form = GarageForm()
    if form.validate_on_submit():
        apiGarageRent.create(publisher=current_user, **form.data)
        return jsonres()

    return jsonres(success=False, msg=u'创建失败')


@bp.route('/garage-<int:id>', methods=['GET'])
def detail_garage():
    garage = apiGarageRent.get_or_404(id)
    return _garage_json(garage)


def _garage_json(garage):
    return dict(id=garage.id,
                price=garage.price,
                position=garage.position,
                contact=garage.contact,
                phone=garage.phone,
                colse=garage.close,
                desc=garage.desc,
                publishTime=mkmillseconds(garage.create_at))
