from sqlalchemy import or_

from ..core import Service
from .models import User, Role


class UserService(Service):
	__model__ = User

class RoleService(Service):
	__model__ = Role
