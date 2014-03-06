from .qingbank import ContactService, DepartmentService, NodeService
from .security import UserService, RoleService

api_contact = ContactService()
api_department = DepartmentService()
api_node = NodeService()

api_user = UserService()
api_role = RoleService()