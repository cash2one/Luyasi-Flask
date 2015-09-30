#-*- coding:utf-8 -*-
from flaskframe.core import Service
from .models import Job, Report
from .forms import JobForm, JobReportForm

class JobService(Service):
    __model__ = Job


class ReportService(Service):
    __model__ = Report
