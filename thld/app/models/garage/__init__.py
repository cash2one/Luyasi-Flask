# -*- coding:utf-8 -*-
from flaskframe.core import Service
from .models import GarageRent


class GarageRentService(Service):
    __model__ = GarageRent

