
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views
urlpatterns = [
    path('signup/' , views.signup, name='signup'),
    path('loginuser' , views.loginuser, name='loginuser'),
    path('logoutuser' , views.logoutuser, name='logoutuser'),
]  