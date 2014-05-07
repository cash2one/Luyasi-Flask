# -*- coding:utf-8 -*-
import importlib
import pkgutil
import logging.handlers
import inspect

from flask import Blueprint
from flask.json import JSONEncoder as BaseJSONEncoder
from flask.ext.admin.contrib.sqla import ModelView

from .core import db

import os


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
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    if app.config['DEBUG_ROUTE']:
        print 'route rules:'
        for rule in app.url_map.iter_rules():
            print rule, rule.endpoint

    return rv

def collect_admin_views(admin):
    """Collect `Flask-Admin <http://flask-admin.readthedocs.org/en/latest/index.html>`_ views in each module"""
    doc_pos = __name__.rfind(r'.')
    parent = __name__[:doc_pos]
    path = os.path.dirname(__file__)
    for _, name, ispkg in pkgutil.walk_packages([path]):
        if ispkg:
            for _, module, ispkg in pkgutil.iter_modules([path + '/' + name]):
                if not ispkg:
                    module_name = '%s.%s.%s' % (parent, name, module)
                    m = importlib.import_module(module_name)
                    for item in dir(m):
                        item = getattr(m, item)
                        if inspect.isclass(item) and issubclass(item, ModelView):
                            admin.add_view(item())
   
                

def import_model(model_path):
    m = importlib.import_module(model_path)
    for item in dir(m):
        item = getattr(m, item)
        print item
        if isinstance(item, db.Model):
            importlib.import_module('%s.%s' % (model_path, item))


class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """
    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
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

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    # def is_valid_json(self, val):
    #     return isinstance(val, (dict,list,int,long,float,True,False,None,str,unicode, db.Model))

    def to_json(self):
        field_names = self.get_field_names()
    
        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
            # 把单独的关联对象，显示为对应的名字
            if isinstance(rv[key], db.Model):
                rv[key] = rv[key].__repr__()
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)

        return rv

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
            smtp = smtplib.SMTP_SSL(self.mailhost, port, timeout=self._timeout)
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
