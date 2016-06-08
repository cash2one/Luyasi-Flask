# -*- coding: utf-8 -*-
"""
   	$(filename)
	~~~~~~~~~~~


    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

import flaskframe.core
from .models import Shop, Item
from flaskframe.ckeditor import CKEditorField

class ShopView(flaskframe.core.AuthModelView):
    column_list = ('name',)
    def __init__(self):
        super(ShopView, self).__init__(Shop, flaskframe.core.db.session, name=u"店铺", endpoint="shops", category=u"店铺管理")


class ItemView(flaskframe.core.AuthModelView):
    column_list = ('name','price')
    def __init__(self):
        super(ItemView, self).__init__(Item, flaskframe.core.db.session, name=u"商品", endpoint="items", category=u"店铺管理")