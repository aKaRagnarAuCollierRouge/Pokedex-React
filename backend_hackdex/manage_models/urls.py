from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('TreeViewModel',TreeModelView.as_view(),name="TreeViewModel")
   
]