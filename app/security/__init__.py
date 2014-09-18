
from ..core import Service
from .models import User, Role, App
from ..xiaoyuan.models import Class


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

class RoleService(Service):
    __model__ = Role