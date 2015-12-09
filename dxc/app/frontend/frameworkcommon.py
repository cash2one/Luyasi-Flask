#-*- coding:utf-8 -*-
from StringIO import StringIO

from flask import Blueprint, send_file, session, request, redirect

from flaskframe.captcha import make_simple_captcha

bp = Blueprint('framework', __name__, template_folder='templates', static_folder='static', url_prefix='/common')

#----------------------------------------------------------------------
@bp.route('/captcha/', methods=['GET'])
def captcha():
    """Return captcha"""
    im, code = make_simple_captcha()
    session['captcha'] = code
    img_io = StringIO()
    im.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@bp.route('/lang/<lang>')
def lang(lang):
    if lang == 'zh':
        session['lang']=lang
        session['moment-lang']='zh-cn'
    else:
        session['lang']=lang
        session['moment-lang']=lang
    url = request.headers.get('Referer')
    return redirect(url)

