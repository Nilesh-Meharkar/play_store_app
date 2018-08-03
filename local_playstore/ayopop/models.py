# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.forms.models import model_to_dict
# Create your models here.


class AppDetails(models.Model):

    # App details
    app_url = models.CharField(max_length=200)
    app_title = models.CharField(max_length=200)
    app_sub_title = models.CharField(max_length=200)
    app_desc = models.CharField(max_length=200)

    # App serach string
    search_str = models.TextField()

    def ayopop_model_to_dict(self):
        return model_to_dict(self)

