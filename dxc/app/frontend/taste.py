# -*- coding: utf-8 -*-
"""

"""
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_security import current_user

from . import route
# from dxc.app.models.wish.forms import WishForm
from dxc.services import api_shop, api_item

bp = Blueprint('taste', __name__, template_folder='templates', static_folder='static', url_prefix='/taste')


@bp.route('/items/<int:page>', methods=['GET'])
@bp.route('/items/', methods=['GET'])
def list_item(page=1):
    if page is None or page <= 0:
        page = 1
    items = api_item.get_lastest_page(page=page)
    return render_template('taste/list_item.html', items=items)


@bp.route('/shops/<int:page>', methods=['GET'])
@bp.route('/shops/', methods=['GET'])
def list_shop(page=1):
    if page is None or page <= 0:
        page = 1
    shops = api_shop.get_lastest_page(page=page)
    return render_template('taste/list_shop.html', shops=shops)