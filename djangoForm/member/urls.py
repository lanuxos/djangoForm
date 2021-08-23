# member urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Add, name='member-page'),
    path('info', views.Info, name='member-info-page'),
]
