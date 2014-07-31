#-*- coding:utf-8 -*-
from ..core import Service
from .models import Academy, Class, Message, MessageUserAssociation

class AcademyService(Service):
    __model__ = Academy


class ClassService(Service):
    __model__ = Class

class MessageService(Service):
    __model__ = Message

    def get_my_msgs(self, user_id):
        query = self.__model__.query.join(self.__model__.user_assocs).filter(
            MessageUserAssociation.user_id == user_id,
            self.__model__.reply_message_id == None
        ).order_by(self.__model__.update_at.desc(), self.__model__.create_at.desc())

        return query