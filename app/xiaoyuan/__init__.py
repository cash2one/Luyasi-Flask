#-*- coding:utf-8 -*-
from ..core import Service
from .models import Academy, Class, Message

class AcademyService(Service):
    __model__ = Academy


class ClassService(Service):
    __model__ = Class


class MessageService(Service):
    __model__ = Message