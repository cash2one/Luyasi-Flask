#-*- coding:utf-8 -*-
# runserver.py 用来启动web server

#解决jinja2在从view返回中文到template会出错的问题。
import sys

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from app import frontend
from app import api
import setting


reload(sys)
sys.setdefaultencoding('utf-8')

# from flask.ext.security import forms

# web应用
frontend_app = frontend.create_app(settings_override=setting)

# api接口
api_app = api.create_app(settings_override=setting)


# 可以分发给不同的app
# application = DispatcherMiddleware(frontend)
# application = DispatcherMiddleware(api_app)
application = DispatcherMiddleware(frontend_app, {'/api': api_app})

if __name__ == "__main__":

    run_simple('127.0.0.1', 5000, application, use_reloader=True, use_debugger=True)
    #If you’re using Aptana/Eclipse for debugging you’ll need to set both use_debugger and use_reloader to False.
    #run_simple('192.168.1.249', 5000, application, use_reloader=False, use_debugger=False, threaded=True)
