from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    #path('',views.post_list, name='post_list'),
    url(r'^$', views.post_list, name='post_list'),
]
