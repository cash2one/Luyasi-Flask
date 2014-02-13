from .qingbank import ContactService, DepartmentService
from .security import UserService, RoleService

api_contact = ContactService()
api_department = DepartmentService()

api_user = UserService()
api_role = RoleService()