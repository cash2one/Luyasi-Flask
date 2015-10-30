#-*- coding:utf-8 -*-

from flask import Blueprint

from dxc.services import api_app
from . import jsonres

bp = Blueprint('api_app', __name__)

#----------------------------------------------------------------------
@bp.route('/appinfo-<appname>', methods=['GET'])
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
