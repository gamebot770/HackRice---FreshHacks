from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.signUp, name='signUp'),
    path('login',views.signIn,name="signIn"),

]
