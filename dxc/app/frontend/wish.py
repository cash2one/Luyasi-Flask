# -*- coding: utf-8 -*-
"""

"""
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_security import current_user

from . import route
from dxc.app.models.wish.forms import WishForm
from dxc.services import api_wish

bp = Blueprint('wish', __name__, template_folder='templates', static_folder='static', url_prefix='/wish')


@bp.route( '/luyasi', methods=['GET', 'POST'])
def luyasi():
    form = WishForm()
    wishes = api_wish.all()
    if form.validate_on_submit():
        job = api_wish.create( **form.data)
        return redirect(url_for('.luyasi'))

    return render_template('wish/luyasi.html', form=form, wishes=wishes)
