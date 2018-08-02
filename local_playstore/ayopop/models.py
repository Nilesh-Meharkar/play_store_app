# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class AppDetails(models.Model):

    # App details
    app_url = models.CharField(max_length=200)
    app_title = models.CharField(max_length=200)
    app_sub_title = models.CharField(max_length=200)
    app_desc = models.CharField(max_length=200)

    # App serach string
    search_str = models.CharField(max_length=200)

