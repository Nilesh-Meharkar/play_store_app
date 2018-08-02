# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from web_scraping_helper import get_play_store_data
# Create your views here.


from django.http import HttpResponse
from django.template import loader


def search(request):

    data = []
    search_str = request.GET.get('search')
    if search_str:
        data = get_play_store_data(search_str)
        data = data[0:12]

    context = {
        'req_data': data,
    }
    return render(request, 'ayopop/app_search.html', context)

