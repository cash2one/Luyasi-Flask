
from sqlalchemy import or_

from ..core import Service
from .models import User, Role, App
from ..xiaoyuan.models import Class
from ..qingbank.models import Contact


class UserService(Service):
    __model__ = User

    #----------------------------------------------------------------------
    def get_user_from_classes(self, class_ids=None, page=1, per_page=20, error_out=True):
        if class_ids is None:
            return None

        query = self.__model__.query.join(self.__model__.classes)\
                        .filter(Class.id.in_(class_ids))\
                        .paginate(page, per_page, error_out)
        return query

    #----------------------------------------------------------------------
    def search_user(self, term):
        query = self.__model__.query.join(self.__model__.contact).filter(or_(
            Contact.name.contains(term),
            self.__model__.username.contains(term),
            self.__model__.email.contains(term)))
        return query


class RoleService(Service):
    __model__ = Role