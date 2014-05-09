#-*- coding:utf-8 -*-

import factory
import factory.alchemy

# import sys
# sys.path.insert(0, 'P:/PythonProjects/FlaskProject/Luyasi-Flask')
# from app.api import create_app
# from tests import test_setting
# appilcation = create_app(settings_override=test_setting)
# print appilcation.name
import app.security.models
import app.qingbank.models
from app.core import db

"""
Factory for generate test datas
"""

class RoleFactory(factory.alchemy.SQLAlchemyModelFactory):
    FACTORY_FOR = app.security.models.Role
    FACTORY_SESSION = db.session

    id = factory.Sequence(lambda n: n)
    name  = factory.Sequence(lambda n: u'Role_%d' % n)

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    FACTORY_FOR = app.security.models.User
    FACTORY_SESSION = db.session

    id = factory.Sequence(lambda n: n)
    email = factory.Sequence(lambda n: u'user_%d@qb.cn' % n)
    password = '123465'

    @factory.post_generation
    def roles(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for role in extracted:
                self.roles.append(role)	

class DepartmentFactory(factory.alchemy.SQLAlchemyModelFactory):
    FACTORY_FOR = app.qingbank.models.Department
    FACTORY_SESSION = db.session
    name = factory.Sequence(lambda n: 'dept_%d' % n)

class ContactFactory(factory.alchemy.SQLAlchemyModelFactory):
    FACTORY_FOR = app.qingbank.models.Contact
    FACTORY_SESSION = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: u'Contact_%d' % n)
    name_pinyin = factory.Sequence(lambda n: u'ct%d' % n)
    name_shot = factory.Sequence(lambda n: u'c%d' % n)

    mobile = factory.Sequence(lambda n: u'mobile_%d' % n)
    telephone = factory.Sequence(lambda n: u'telephone_%d' % n)
    innerphone = factory.Sequence(lambda n: u'innerphone_%d' % n)
    fax = factory.Sequence(lambda n: u'fax_%d' % n)
    qq = factory.Sequence(lambda n: u'qq_%d' % n)
    description = factory.Sequence(lambda n: u'description_%d' % n)

    # department_id = db.Column(db.Integer(), db.ForeignKey('qingbank_department.id'))
    department = factory.SubFactory(DepartmentFactory)

    # user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    user = factory.SubFactory(UserFactory)