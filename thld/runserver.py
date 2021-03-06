# -*- coding:utf-8 -*-
# runserver.py 用来启动web server

# 解决jinja2在从view返回中文到template会出错的问题。
import sys

from flask import  request
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

sys.path.insert(0, '/home/flask/Luyasi-Flask')

# from app import thld_web
from app import api
from thld import setting

reload(sys)
sys.setdefaultencoding('utf-8')

# from flask.ext.security import forms

# web应用
# frontend_app = thld_web.create_app(settings_override=setting)

# api接口
api_app = api.create_app(settings_override=setting)

# apps = [{'api_id': 'app0001', 'app_key': '12345678', 'app_type': 'web'}]
#
#
# @api_app.before_first_request
# def api_gateway():
#     api_id = request.args.get('api_id')
#     print api_id
#     return js


# 可以分发给不同的app
# application = DispatcherMiddleware(frontend)
# application = DispatcherMiddleware(api_app)
application = DispatcherMiddleware(api_app, {'/api': api_app})

if __name__ == "__main__":
    print u'App thld starts:'
    ip = api_app.config['KINORSI_SERVER_NAME']
    port = api_app.config['KINORSI_SERVER_PORT']
    # run_simple('127.0.0.1', 5000, application, use_reloader=True, use_debugger=True)
    # If you’re using Aptana/Eclipse for debugging you’ll need to set both use_debugger and use_reloader to False.
    run_simple(ip, port, application, use_reloader=False, use_debugger=False, threaded=True)
