#-*- coding:utf-8 -*-
from flaskframe.core import Service
from .models import CarpoolInfo
from .forms import CarpoolForm

class CarpoolInfoService(Service):
    __model__ = CarpoolInfo

