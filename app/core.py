#-*- coding:utf-8 -*-
# from flask_mail import Mail
from collections import namedtuple

from flask_admin import Admin
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, event, asc, desc
from sqlalchemy.orm import mapper
from flask_babel import Babel
from flask_mail import Mail
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

import datetime
# Flask-SQLAlchemy extension instance
# Version 1.0 Flask-SQLalchemy autoflush default value is False. Here let it be True.
db = SQLAlchemy(session_options={'autocommit': False, 'autoflush': True})

def before_update(mapper, connection, target):
    target.update_at = datetime.datetime.utcnow()

def before_insert(mapper, connection, target):
    now = datetime.datetime.utcnow()
    target.create_at = now
    target.update_at = now


# 使用mapper用来使全局有效
event.listen(mapper, 'before_update', before_update)
event.listen(mapper, 'before_insert', before_insert)


class ModelVersion(object):
    """Predefine some columns.
    :attr:`update_at`, for recording update time.
    :attr:`create_at`, for recording create time.
    :attr:`version`, for optimistic locking.
    """
    #: Datetime for updation of this record. :method:`before_update` to update this.
    update_at = db.Column(db.DateTime())

    #: Datetime for creation of this record.
    create_at = db.Column(db.DateTime())

# 修改sqlalchemy生成约束时的命名规则。其中要注意ck，这是个check，这样以后在定义db.Boolean的时候要加个name:db.Boolean(name='sth')
convention = {
    "ix": 'ix__%(column_0_label)s',
    "uq": "uq__%(table_name)s__%(column_0_name)s",
    # mysql 不支持check constraint
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": "fk__%(table_name)s__%(column_0_name)s__%(referred_table_name)s",
    "pk": "pk__%(table_name)s"
}
db.metadata.naming_convention=convention

# Flask-Admin extension instance - 在测试中会重复给admin.add_views而出现bug，所以admin的初始化最好放在create_app中
# admin = Admin(name='Admin', base_template='admin/admin_base.html')

# Flask-Mail extension instance
mail = Mail()

# Flask-Security extension instance
security = Security()

# Flask-Babel
babel = Babel()

# pricipal need for right
RightNeed = namedtuple('RightNeed', ['action', 'app', 'entity'])
# 控制管理面板FLask-Admin的权限
class AuthModelView(ModelView):
    """Subclass of :class:`flask.ext.admin.contrib.sqla.ModelView`. This view need spedific roles to access.
    """

    #: roles allowed to access this type views.
    allowedRoles = ()

    def is_accessible(self):
        """return True if accessable."""
        return  current_user.has_role(u'超级管理员') or self._hasAllowedRole()
        #return  current_user.is_authenticated() #最好用角色

    def _hasAllowedRole(self):
        """Has allowed roles or not."""
        for r in self.allowedRoles:
            if current_user.has_role(r):
                return True
        return False

class LuyasiFormError(Exception):
    """Raise when an error processing a form occurs."""

    def __init__(self, errors=None):
        self.errors = errors

class LuyasiError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Service(object):
    """A :class:`Service` instance encapsulates common SQLAlchemy model
    operations in the context of a :class:`Flask` application.
    """
    __model__ = None

    def _isinstance(self, model, raise_error=True):
        """Checks if the specified model instance matches the service's model.
        By default this method will raise a `ValueError` if the model is not the
        expected type.

        :param model: the model instance to check
        :param raise_error: flag to raise an error on a mismatch
        """
        rv = isinstance(model, self.__model__)
        if not rv and raise_error:
            raise ValueError('%s is not of type %s' % (model, self.__model__))
        return rv

    def _preprocess_params(self, kwargs):
        """Returns a preprocessed dictionary of parameters. Used by default
        before creating a new instance or updating an existing instance.

        :param kwargs: a dictionary of parameters
        """
        kwargs.pop('csrf_token', None)
        kwargs.pop('captcha', None)
        return kwargs

    def save(self, model):
        """Commits the model to the database and returns the model

        :param model: the model to save
        """
        self._isinstance(model)
        db.session.add(model)
        db.session.commit()
        return model

    def all(self):
        """Returns a generator containing all instances of the service's model.
        """
        return self.__model__.query.all()

    def get_page(self, page, per_page=20, error_out=True):
        return self.__model__.query.paginate(page, per_page, error_out)

    def get(self, id):
        """Returns an instance of the service's model with the specified id.
        Returns `None` if an instance with the specified id does not exist.

        :param id: the instance id
        """
        return self.__model__.query.get(id)

    def get_all(self, *ids):
        """Returns a list of instances of the service's model with the specified
        ids.

        :param ids: instance ids
        """
        return self.__model__.query.filter(self.__model__.id.in_(ids)).all()

    def find(self, **kwargs):
        """Returns a list of instances of the service's model filtered by the
        specified key word arguments.

        :param kwargs: filter parameters
        """
        return self.__model__.query.filter_by(**kwargs)

    def first(self, **kwargs):
        """Returns the first instance found of the service's model filtered by
        the specified key word arguments.

        :param kwargs: filter parameters
        """
        return self.find(**kwargs).first()

    def get_or_404(self, id):
        """Returns an instance of the service's model with the specified id or
        raises an 404 error if an instance with the specified id does not exist.

        :param id: the instance id
        """
        return self.__model__.query.get_or_404(id)

    def new(self, **kwargs):
        """Returns a new, unsaved instance of the service's model class.

        :param kwargs: instance parameters
        """
        return self.__model__(**self._preprocess_params(kwargs))

    def create(self, **kwargs):
        """Returns a new, saved instance of the service's model class.

        :param kwargs: instance parameters
        """
        return self.save(self.new(**kwargs))

    def update(self, model, **kwargs):
        """Returns an updated instance of the service's model class.

        :param model: the model to update
        :param kwargs: update parameters
        """
        self._isinstance(model)
        for k, v in self._preprocess_params(kwargs).items():
            setattr(model, k, v)
        self.save(model)
        return model

    def delete(self, model):
        """Immediately deletes the specified model instance.

        :param model: the model instance to delete
        """
        self._isinstance(model)
        db.session.delete(model)
        db.session.commit()

    #----------------------------------------------------------------------
    def get_page_filterby(self, page=1, per_page=20, error_out=True, **kwargs):
        """Get a page that has been filtered.
        """
        return self.__model__.query.filter_by(**kwargs).paginate(page, per_page, error_out)

    #----------------------------------------------------------------------
    def get_latest_page_filterby(self, page=1, per_page=20, error_out=True, **kwargs):
        """
        """
        return self.__model__.query \
                .filter_by(**kwargs) \
                .order_by(self.__model__.update_at.desc(), self.__model__.create_at.desc()) \
                .paginate(page, per_page, error_out)

    #----------------------------------------------------------------------
    def get_lastest_page(self, page, per_page=20, error_out=True):
        """"""
        return self.__model__.query \
                .order_by(self.__model__.update_at.desc(), self.__model__.create_at.desc()) \
                .paginate(page, per_page, error_out)