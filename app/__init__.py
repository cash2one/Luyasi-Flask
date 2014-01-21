# # -*- coding:utf-8 -*-

# from flask import Flask, render_template, jsonify

# from flask.ext.sqlalchemy import SQLAlchemy
# from app.helpers import JSONEncoder

# app = Flask(__name__)
# #修改默认的flask json encoder
# app.json_encoder = JSONEncoder

# #直接读取Luyasi/config.py
# app.config.from_object('config')
# db = SQLAlchemy(app)


# # 以下用来引入其它的app并注册blueprint
# # qingbank 模块
# from app.qingbank.models import *
# import api.qingbank
# app.register_blueprint(api.qingbank.bp_contact)
# app.register_blueprint(api.qingbank.bp_department)

# # 注册api的错误处理


# @app.errorhandler(404)
# def not_found(error):
# 	return render_template('404.html'), 404

# def on_luyasi_error(e):
#     return jsonify(dict(error=e.msg)), 400

# def on_luyasi_form_error(e):
#     return jsonify(dict(errors=e.errors)), 400

# def on_404(e):
#     return jsonify(dict(error='Not found')), 404

# from .core import LuyasiError, LuyasiFormError
# app.errorhandler(LuyasiError)(on_luyasi_error)
# app.errorhandler(LuyasiFormError)(on_luyasi_form_error)

# # api模块
# # from app.apirouter import apirouter as apiRouter
# # app.register_blueprint(apiRouter, url_prefix='/rest')