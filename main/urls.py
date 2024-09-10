from django.shortcuts import render
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('halo', show_main, name='show_main'),
]