#-*- coding:utf-8 -*-

from .qingbank import ContactService, DepartmentService, NodeService
from .security import UserService, RoleService
from .blog	import CommentService, BlogService
from .job import JobService, ReportService

api_contact = ContactService()
api_department = DepartmentService()
api_node = NodeService()

# security
api_user = UserService()
api_role = RoleService()

# blog
api_blog = BlogService()
api_comment = CommentService()

#job
api_job = JobService()
api_report = ReportService()