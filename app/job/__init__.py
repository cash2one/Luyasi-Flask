#-*- coding:utf-8 -*-
from ..core import Service
from .models import Job

class JobService(Service):
    __model__ = Job

