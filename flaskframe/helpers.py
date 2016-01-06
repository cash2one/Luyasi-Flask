# -*- coding:utf-8 -*-
import importlib
import pkgutil
import logging.handlers
import inspect
import time
import os

from itsdangerous import Signer, BadSignature
from flask import Blueprint, current_app, request, abort, jsonify, url_for
from flask.json import JSONEncoder as BaseJSONEncoder
from flask.ext.admin.contrib.sqla import ModelView
from flask_security import current_user

from flaskframe.core import db


def register_blueprints(app, package_name, package_path):
    """
    Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :param app: the Flask application
    :param package_name: the package name
    :param package_path: the package path
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        # print str.format("packagename:{}---module name:{}", package_name, name)
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)

    # 注册通用api
    from flaskframe.security import api
    app.register_blueprint(api.bp)

    if app.config['DEBUG_PRINT_ROUTE']:
        print 'route rules:'
        for rule in app.url_map.iter_rules():
            print rule, rule.endpoint

    return rv


def collect_admin_views(package, admin, app):
    """自动收集所有的管理视图
    :param package 包
    :param admin admin应用
    :param app app实例
    """

    # 单独把flaskframe里的用户model加一下
    from flaskframe.security.views import AppView, RightView, RoleView, UserView
    admin.add_view(AppView())
    admin.add_view(RightView())
    admin.add_view(RoleView())
    admin.add_view(UserView())

    appname = app.config['APP_NAME']
    path = os.path.dirname(package.__file__)
    for _, name, ispkg in pkgutil.walk_packages([path]):
        if ispkg:
            for _, module_name, ispkg in pkgutil.iter_modules([path + '/' + name]):
                if not ispkg and module_name == 'views':
                    module_name = '%s.%s.%s.%s' % (appname, package.__name__, name, module_name)
                    m = importlib.import_module(module_name)
                    for item in dir(m):
                        item = getattr(m, item)
                        if inspect.isclass(item) and issubclass(item, ModelView):
                            admin.add_view(item())


def import_model(model_path):
    m = importlib.import_module(model_path)
    for item in dir(m):
        item = getattr(m, item)
        # print item
        if isinstance(item, db.Model):
            importlib.import_module('%s.%s' % (model_path, item))


class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """

    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            self.max_depth = current_app.config['SQLALCHMY_MAX_DEPTH']
            return obj.to_json(self.max_depth)
        return super(JSONEncoder, self).default(obj)


class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None
    #: Field in this collect is not limited by the depth.
    __json_depth_no_limit__ = None

    # --------------------------------------------------------------
    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    # def is_valid_json(self, val):
    #     return isinstance(val, (dict,list,int,long,float,True,False,None,str,unicode, db.Model))

    # --------------------------------------------------------------
    def to_json(self, max_depth):
        """Just filter the fields which will be left for json to encode.
        """
        # 用来控制json的返回深度
        max_depth -= 1

        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        depth_no_limit = self.__json_depth_no_limit__ or []

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        # 可能出现多层次的递归。
        rvfinal = dict()
        for key in rv:
            # 注意：移除不能被tojson的属性~即如果是类的属性，但是却没有继承JsonSerializer的话就移除。
            # AppenderBaseQuery似乎是生成的类，在文件里找不到。所以只能用名字。

            # 处理集合的情况，要取一个元素出来比较其类型是否为JsonSerialzer。
            test = rv[key]
            is_collect = False
            if isinstance(rv[key], (list, dict)) and len(rv[key]) > 0:
                is_collect = True
                test = rv[key][0]

            # 如果是可以serializer的类型。如果已经达到最大深度了，则返回__repr__()的表示。如果没有的话则继续向下。
            # 对于集体的处理则要对间个元素进行深度测试。
            if isinstance(test, JsonSerializer):
                if max_depth == 0 and key not in depth_no_limit:
                    rvfinal[key] = rv[key].__repr__()
                else:
                    if not is_collect:
                        rvfinal[key] = rv[key].to_json(max_depth)
                    else:  # is_collect = True
                        json_list = list()
                        for item in rv[key]:
                            json_list.append(item.to_json(max_depth))
                        rvfinal[key] = json_list
                continue
            elif rv[key] and type(rv[key]).__name__ == 'AppenderBaseQuery':
                continue

            rvfinal[key] = rv[key]

        return rvfinal


##############################################################
class TlsSMTPHandler(logging.handlers.SMTPHandler):
    """Gmail should use this to do email logging. But it seems not work!"""

    def emit(self, record):
        """
        Emit a record.
        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            import string  # for tls add this line
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                self.fromaddr,
                string.join(self.toaddrs, ","),
                self.getSubject(record),
                formatdate(), msg)
            if self.username:
                smtp.ehlo()  # for tls add this line
                smtp.starttls()  # for tls add this line
                smtp.ehlo()  # for tls add this line
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


##############################################################
class SslSTMPHandler(logging.handlers.SMTPHandler):
    """When use SSL, need to use this. Currently used with QQEmail"""

    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            from email.utils import formatdate
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP_SSL(self.mailhost, port)  # , timeout=self._timeout)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                self.fromaddr,
                ",".join(self.toaddrs),
                self.getSubject(record),
                formatdate(), msg)
            if self.username:
                if self.secure is not None:
                    smtp.ehlo()
                    smtp.starttls(*self.secure)
                    smtp.ehlo()
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


# ----------------------------------------------------------------------
def mkmillseconds(datetime):
    """转成毫秒值"""
    # return time.mktime(datetime.timetuple()) * 1000
    return int(time.time()) * 1000


def check_app_key():
    """在before_request里检查appid"""
    apps = [{'app_id': 'app0001', 'app_key': '12345678', 'app_type': 'web'}]
    appids = [app['app_id'] for app in apps]
    """注册到before_request，检查调用api的应用是否在注册列表，如果不在的话，就没得玩啦"""
    # for he in request.headers:
    #     print he
    app_id = request.headers.get('app_id') or request.args.get('app_id')
    if app_id is None or app_id not in appids:
        abort(403)

    # flask-security提供的登陆服务直接被卡掉
    if request.path == url_for(current_app.config['SECURITY_BLUEPRINT_NAME'] + '.login'):
        abort(404)

    # app类型检测
    app_type = None
    for app in apps:
        if app['app_id'] == app_id:
            app_type = app['app_type']
    if app_type == 'web':
        # 登陆的相关的就不检查了，其它的才检查
        if request.blueprint not in [current_app.config['SECURITY_BLUEPRINT_NAME'], 'api_login']:
            if request.method in ['POST', 'DELETE', 'DELETE']:
                # 只检查这些有个改能力的操作
                csrf_token = request.headers.get('X-XSRF-TOKEN')
                valid = validate_csrf_token(csrf_token)
                if not valid:
                    return jsonres(success=False, msg=u'csrf_token无效或超时')

    elif app_type == 'mobile':
        # 不检查csrf
        pass
    else:
        # 没有授权的应用
        abort(401)

    pass


def generate_csrf_token(user):
    """产生token"""
    secret_key = current_app.config.get(
        'WTF_CSRF_SECRET_KEY', current_app.secret_key
    )
    nonce = os.urandom(24)
    user_id = user.id
    signer = Signer(secret_key)
    csrf_token = signer.sign(str(user_id))
    print csrf_token
    return csrf_token


def validate_csrf_token(csrf_token):
    secret_key = current_app.config.get(
        'WTF_CSRF_SECRET_KEY', current_app.secret_key
    )
    signer = Signer(secret_key)
    # if current_user.is_anonymous():
    #     return False

    try:
        signer.unsign(csrf_token)
    except BadSignature:
        return False

    # if str(current_user.get_id()) == id:
    #     return True
    return True
#
# def require_api_key(api_method):
#     """用来检查调用者是否是授权的app"""
#     @wraps(api_method)
#     def check_api_key(*arg, **kwargs):
#         api_id = request.headers.get('api_id')
#
#         if api_id and api_id == '1111':
#             return api_method(*arg, **kwargs)
#         else:
#             abort(401)
#
#     return check_api_key

def jsonres(rv=None, metacode=200, msg='', code=200, success=True):
    '''这样api可以返回一致的结构。
    @param rv 主要的返回内容
    @param metacode 业务上的代码
    @param msg 简要信息
    @param desc 详细描述
    @param code 这是http返回的statucode
    @param success metacode有点复杂，一般用这个来表示请求是否成功吧
    '''
    #    code = 200
    #   msg = ''
    # if isinstance(res, tuple):
    # rv = res[0]
    # code = res[1]
    # if len(res)==3:
    # msg = res[2]
    return jsonify(dict(response=rv, meta=dict(code=metacode, msg=msg, success=success))), code
