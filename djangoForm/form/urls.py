# form urls.py
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('add', Add, name='add-page'),
]
