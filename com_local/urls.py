# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import index, new_request, RequestCarsList, RequestsView, RequestsViewJson

urlpatterns = patterns('',
    ##url(r'^$', views.index, name='index'),
    ##url(r'^add/$', views.ClassifiedCreate.as_view(), name='new'),
    url(r'^$', index, name='home'),
    #url(r'^request/list/$', RequestsView.as_view(), name='request_list'),
    url(r'^request/list/$', RequestsViewJson.as_view(), name='request_list'),
    url(r'^request/new/$', new_request, name='new_request'),
    url(r'^request/view/(?P<pk>\d+)/$', RequestCarsList.as_view(), name='request_cars'),
)