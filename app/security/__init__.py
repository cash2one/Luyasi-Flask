
from ..core import Service
from .models import User, Role, App
from ..xiaoyuan.models import Class


class UserService(Service):
    __model__ = User

    #----------------------------------------------------------------------
    def get_user_from_classes(self, class_ids=None):
        if class_ids is None:
            return None

        query = self.__model__.query.join(self.__model__.classes).filter(Class.id.in_(class_ids))
        return query

class RoleService(Service):
    __model__ = Role