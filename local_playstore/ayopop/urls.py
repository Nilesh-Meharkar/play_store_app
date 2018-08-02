from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.search, name='index'),
    # url(r'^(?P<search_str>\w+)$', views.results, name='results'),
]