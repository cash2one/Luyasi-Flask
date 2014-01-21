# # -*- coding: utf-8 -*-  
# #所有的请求都可以从这里进，由这个统一入口进对请求进行分发
# '''
# http://host:port/rest?sign=***&timestamp=***&v=**&app_key=**&method=qingbank.contactinfo.create&format=xml&session=test&fields=nick
# '''

# from flask import Blueprint, render_template, abort, request, jsonify


# apirouter = Blueprint('apirouter', __name__)

# @apirouter.route('/')
# def router():
# 	# return jsonify(name='ki', age=20)
# 	# appid = request.args.get('appid', '')
# 	# timestamp = request.args.get('timestamp', '')
# 	# v = request.args.get('v', '')
# 	# sign = request.args.get('sign', '')
# 	# sign = request.args.get('sign_method', '')
# 	api = request.args.get('api', '')
# 	# session = request.args.get('session', '')
# 	dot = api.rfind('.')
# 	pack = api[:dot]
# 	method = api[dot+1:]
# 	importstatement = 'from %s import %s' %(pack, method)
# 	exec(importstatement)
# 	fun = eval(method)
# 	fun_varnames = fun.func_code.co_varnames[:fun.func_code.co_argcount]
# 	params = {}
# 	for var in fun_varnames:
# 		params[str(var)] = request.args.get(str(var), '')
# 	print params
# 	print str(fun.__name__)
# 	res = fun(**params)	
# 	print res
# 	return 'ok'

