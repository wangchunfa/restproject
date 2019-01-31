#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 0023 18:15
# @Author  : chunfa.wang
# @Email   : wang_chun_fa@163.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from drest import views

urlpatterns = [
    url(r'^user/$', views.list_user),
    url(r'^user/add/$', views.add_user),
    url(r'^user/del/$', views.del_user),
]

