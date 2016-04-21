from flask import Blueprint, request
from flask_security import current_user

from flaskframe.helpers import mkmillseconds, paginationInfo
from dxc.services import api_class
from . import  jsonres, route
from dxc.app.models.blog import BlogForm, BlogUpdateForm
from dxc.app.models.xiaoyuan import MessageUserAssociation, ClassUserAssociation


bp = Blueprint('api_xiaoyuan', __name__, url_prefix='/xiaoyuan')