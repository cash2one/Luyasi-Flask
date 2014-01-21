from .models import Department, Contact
from ..core import Service
from sqlalchemy import or_

class ContactService(Service):
	__model__ = Contact

	def search(self, keyword):
		query = self.__model__.query.filter(or_(
			self.__model__.name_pinyin.startswith(keyword), 
			self.__model__.name_shot.startswith(keyword),
			self.__model__.name.startswith(keyword)))
		return query

class DepartmentService(Service):
	__model__ = Department

