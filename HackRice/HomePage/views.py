from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
import requests
import json
from django.shortcuts import redirect
import datetime
from .models import *
# Create your views here.

def HomePage(request):
    return HttpResponse("<h1>ji</h1>")

def aboutPage(request):
    a=2
    b=4
    sum = a + b

    customers = getCustomers()
    for customer in customers:
        print(customer["_id"],getPurchases(str(customer["_id"])))
    return render(request,"HomePage/example.html",{"sum":sum})