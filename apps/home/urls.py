from django.contrib import admin
from django.urls import path, include
from .views.views import index
# from . import settings

urlpatterns = [
    path('', index),
]
