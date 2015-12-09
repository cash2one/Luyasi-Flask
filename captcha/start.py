# -*- coding:utf-8 -*-

from StringIO import StringIO
import random

from flask import Flask, session, request, send_file, Blueprint, json
from werkzeug.serving import run_simple

from flaskframe.captcha import make_simple_captcha

captchaApp = Flask("CaptchaService")
captchaApp.secret_key = "\x80\xe8\xe8\xba)\xc6\xcc\x17\xd4k\x84\xdd\xe3%\xa70v]\x1b\xc2l\xfe\xc6-"

bp = Blueprint("captcha-service", __name__, url_prefix="/captcha")


@bp.route('/', methods=['GET'])
def captcha():
    im, code = make_simple_captcha(width=120, height=36, font_sizes=random.sample(range(40,50), 4))
    session['captcha'] = code
    img_io = StringIO()
    im.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@bp.route('/check/', methods=['GET'])
def check_captcha():
    code = request.args.get('captcha_code')
    real_code = session['captcha']
    if code is None or real_code is None:
        return json.jsonify(dict( meta=dict(success=False))), 200
    if code.upper() == real_code:
        return json.jsonify(dict( meta=dict(success=True))), 200
    else:
        return json.jsonify(dict( meta=dict(success=False))), 200

captchaApp.register_blueprint(bp)

if __name__ == "__main__":
    run_simple('127.0.0.1', 5000, captchaApp, use_reloader=False, use_debugger=True)
    # If you’re using Aptana/Eclipse for debugging you’ll need to set both use_debugger and use_reloader to False.
