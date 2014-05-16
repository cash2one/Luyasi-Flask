#-*- coding: utf-8 -*-
from ..core import Service
from .models import Contact, Department, DocNode


class ContactService(Service):
    """Contact api service.
    """

    __model__ = Contact

    def search(self, keyword):
        query = self.__model__.query.join(self.__model__.department).filter(or_(
            Department.name.contains(keyword),
            self.__model__.mobile.contains(keyword),
            self.__model__.telephone.contains(keyword),
            self.__model__.fax.contains(keyword),
            self.__model__.innerphone.contains(keyword),
            self.__model__.name_pinyin.startswith(keyword), 
            self.__model__.name_shot.startswith(keyword),
            self.__model__.name.startswith(keyword)))
        return query

class DepartmentService(Service):
    """Department api service.
    """

    __model__ = Department

class NodeService(Service):
    """Node api service.
    """
    __model__ = DocNode