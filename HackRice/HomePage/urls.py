from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('about',views.aboutPage,name="aboutPage"),
    path('login',views.login,name="login"),
    #path("dashboard",views.dashboard,name="dashboard"),
    path("categorySelection",views.categorySelection,name="categorySelection"),

    path("baseTemplate",views.baseTemplate,name="baseTemplate"),
    path("transactionUpdate",views.transactionUpdate,name="transactionUpdate"),

    path("signUp",views.signUp,name="signUpPage"),
    path("dashboard",views.dashboard,name="dashboard"),
]
