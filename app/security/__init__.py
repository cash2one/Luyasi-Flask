
from sqlalchemy import or_

from ..core import Service
from .models import User, Role, App, Profile, SysMessage
from ..xiaoyuan.models import Class
from ..qingbank.models import Contact


class UserService(Service):
    __model__ = User

    #----------------------------------------------------------------------
    def get_user_from_classes(self, class_ids=None, role_ids=None, page=1, per_page=20, error_out=True):
        if class_ids is None:
            return None

        query = self.__model__.query.join(self.__model__.classes).join(self.__model__.roles)\
                        .filter(Class.id.in_(class_ids))\
                        .filter(Role.id.in_(role_ids))\
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
    
class ProfileService(Service):
    __model__ = Profile
    
class SysMessageService(Service):
    __model__ = SysMessage