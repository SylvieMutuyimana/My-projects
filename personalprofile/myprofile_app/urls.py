from django.contrib import admin
from django.urls import path, include

from myprofile_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check', views.check, name='check'),
]
