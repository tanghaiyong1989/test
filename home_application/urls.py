# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    url(r'^test1/', include('test1.urls')),
)
