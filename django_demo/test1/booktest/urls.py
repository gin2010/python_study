# -*- coding: utf-8 -*-
# File  : urls.py
# Author: water
# Date  : 2020/1/11
# Desc  : 
from django.conf.urls import include, url
from booktest import views
# booktest的urls文件
urlpatterns = [
    url(r'^index/$', views.index),   # 建议index与index()中的关系
    url(r'^books/$', views.show_books), # 展示全部图书
    url(r'^books/(\d+)$', views.details), # 展示详细信息
]
