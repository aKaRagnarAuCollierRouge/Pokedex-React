from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("CreateAccount/",CreateAccount.as_view(),name="createaccount"),
    path("Login/",LoginView.as_view(),name='LoginView')
    

]