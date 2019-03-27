# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import data
from .models import login
# Register your models here.
admin.site.register(data)
admin.site.register(login)
