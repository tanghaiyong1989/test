# -*- coding: utf-8 -*-
# from django.conf.urls import url,include
from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    # (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^helloworld/$', 'helloworld'),
)
