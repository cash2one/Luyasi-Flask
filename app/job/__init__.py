#-*- coding:utf-8 -*-
from ..core import Service
from .models import Job, Report

class JobService(Service):
    __model__ = Job


class ReportService(Service):
    __model__ = Report
