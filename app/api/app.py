#-*- coding:utf-8 -*-

import time

from flask import Blueprint, request,jsonify
from flask.ext.babel import gettext

from . import route, jsonres
from ..core import LuyasiError, LuyasiFormError
from ..services import api_app
from ..helpers import mkmillseconds
from . import paginationInfo, jsonres

bp = Blueprint('api_app', __name__, url_prefix='/app')

#----------------------------------------------------------------------
@bp.route('/info-<appname>', methods=['GET'])
def appinfo(appname):
    """"""
    app = api_app.first(name=appname)
    return jsonres(rv=dict(
        appname=app.name,
        app_version=app.app_version,
        app_vercode=app.app_vercode,
        app_update_url=app.update_url,
        update_url="http://0763dxc.com"
    ))
