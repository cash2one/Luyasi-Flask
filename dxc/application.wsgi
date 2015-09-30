#-*- coding:utf-8 -*-
# run.py 用来启动web server
# from app import app

#激活虚拟机环境
activate_this = 'P:/PythonProjects/FlaskProject/venv/Scripts/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
# app.run(debug=True)
#解决jinja2在从view返回中文到template会出错的问题。
import sys
#需要加入这些路径才能找到
#sys.path.insert(0, 'P:/PythonProjects/FlaskProject/Luyasi-Flask/app')
sys.path.insert(0, 'P:/PythonProjects/FlaskProject/Luyasi-Flask')

from app import api, frontend
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

reload(sys)
sys.setdefaultencoding('utf-8')


from flask.ext.security import forms

#api接口
api_app = api.create_app()
#web应用
frontend_app = frontend.create_app()

# 可以分发给不同的app
application = DispatcherMiddleware(frontend_app, {'/api': api_app})

