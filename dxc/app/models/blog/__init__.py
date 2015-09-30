#-*- coding:utf-8 -*-
from flaskframe.core import Service
from .models import Blog, Comment, Category
from .forms import BlogForm, CommentForm, BlogUpdateForm

class BlogService(Service):
    __model__ = Blog

class CommentService(Service):
    __model__ = Comment

class CategoryService(Service):
    __model__ = Category