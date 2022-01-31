from django.contrib import admin
from django.urls import re_path, include
from . import views

urlpatterns = [
   re_path('', views.myFirstChart , name="demo"),
]
