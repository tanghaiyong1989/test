#coding:utf-8
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$',test1,name='modify_backstage'),
]