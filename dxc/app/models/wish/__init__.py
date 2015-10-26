# -*- coding:utf-8 -*-

from flaskframe.core import Service
from .models import Wish
from .forms import WishForm


class WishService(Service):
    __model__ = Wish

