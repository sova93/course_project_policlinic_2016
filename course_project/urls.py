# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from Policlinic.views import *

urlpatterns = patterns('',
    ('^$',index),
    ('^search_client_id/$', search_client_id),
    ('^statistics_view/$', statistics_view),
    ('^search_client_surename/$', search_client_surename),
    ('^search_plot_client/$', search_plot_client),
    ('^search_doctor_spec/$', search_doctor_spec),
    ('^statistics_group_view/$', statistics_group_view),
    ('^contacts/$', contacts),
    ('^view_disease/$', view_disease),
    ('^view_doctors/$', view_doctors),
    ('^view_clients/$', view_clients),
    url(r'^admin/', include(admin.site.urls)),
)
