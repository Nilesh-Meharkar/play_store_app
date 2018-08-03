# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from utils import get_search_data
from models import AppDetails
# Create your views here.


from django.http import HttpResponse
from django.template import loader


def search(request):

    data = []
    search_str = request.GET.get('search')
    if search_str:
        data = get_search_data(search_str)

    context = {
        'req_data': data,
    }
    return render(request, 'ayopop/app_search.html', context)


def details(request, id):

    app_obj = AppDetails.objects.get(id=id)
    app_dict = app_obj.ayopop_model_to_dict()
    context = {
        'req_data': [app_dict]
    }

    return render(request, 'ayopop/details.html', context)

