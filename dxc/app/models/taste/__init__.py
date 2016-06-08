#-*- coding:utf-8 -*-
from flaskframe.core import Service
from .models import Shop, Item


class ShopService(Service):
    __model__ = Shop


class ItemtService(Service):
    __model__ = Item
