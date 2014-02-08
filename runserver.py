#-*- coding:utf-8 -*-
# run.py 用来启动web server
# from app import app


# app.run(debug=True)
#解决jinja2在从view返回中文到template会出错的问题。
import sys

from app import api, frontend
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

reload(sys)
sys.setdefaultencoding('utf-8')


#api接口
api_app = api.create_app()
#web应用
frontend_app = frontend.create_app()

# 可以分发给不同的app
application = DispatcherMiddleware(frontend_app, {'/api': api_app})

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
