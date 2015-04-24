#-*- coding:utf-8 -*-

from .qingbank import ContactService, DepartmentService, NodeService
from .security import UserService, RoleService, ProfileService, SysMessageService
from .blog import CommentService, BlogService
from .job import JobService, ReportService
from .carpool import CarpoolInfoService
from .xiaoyuan import AcademyService, ClassService, MessageService, ClassApplyService, NoticeService

api_contact = ContactService()
api_department = DepartmentService()
api_node = NodeService()

# security
api_user = UserService()
api_role = RoleService()
api_profile = ProfileService()
api_sysmsg = SysMessageService()

# blog
api_blog = BlogService()
api_comment = CommentService()

#job
api_job = JobService()
api_report = ReportService()

#carpool
api_carpool = CarpoolInfoService()

#xiaoyuan
api_academy = AcademyService()
api_class = ClassService()
api_msg = MessageService()
api_apply = ClassApplyService()
#api_meminfo = MemberInfoService()
api_notice = NoticeService()