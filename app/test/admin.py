# -*- coding: utf8 -*-
from .models import TestCase, TestCaseExample, TestCasePass
from django.contrib import admin

admin.site.register(TestCase)
admin.site.register(TestCaseExample)
admin.site.register(TestCasePass)
