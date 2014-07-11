# -*- coding: utf-8 -*-

from flask import redirect, url_for, request, render_template, Blueprint

from . import route

from ..carpool.forms import CarpoolForm
from ..services import api_carpool

bp = Blueprint('carpool', __name__, template_folder='templates', static_folder='static', url_prefix='/carpool')

#----------------------------------------------------------------------
@route(bp, '/new', methods=['GET', 'POST'])
def create_carinfo():
	""""""
	form = CarpoolForm()
	if form.validate_on_submit():
		carinfo = api_carpool.create(user=None, **form.data)
		return url_for('.detail_carinfo', carinfo_id=carinfo.id)
	return render_template('carpool/create.html', form=form)

#----------------------------------------------------------------------
@route(bp, '/change/<int:carinfo_id>')
def change_carinfo(carinfo_id):
	""""""
	carinfo = api_carpool.get(carinfo_id)
	form = CarpoolForm(obj=carinfo)
	return render_template('carpool/create.html', form)


#----------------------------------------------------------------------
@bp.route('/detail/<int:carinfo_id>', methods=['GET'])
def detail_carinfo(carinfo_id):
	carinfo = api_carpool.get(carinfo_id)
	return render_template('carpool/detail.html', carinfo=carinfo)


#----------------------------------------------------------------------
@bp.route('/<int:page>', methods=['GET'])
@bp.route('/', methods=['GET'])
def list_carinfo(page=None):
	if page == None or page <= 0:
		page = 1
	carinfos = api_carpool.get_lastest_page(page)
	return render_template('carpool/list.html', carinfos = carinfos)
#----------------------------------------------------------------------
def delete_carinfo():
	pass


