from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('add/', add_document, name='add_document'),
    path('search/', search_document, name='search_document'),
]