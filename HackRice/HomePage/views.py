from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
import requests
import json
from django.shortcuts import redirect
import datetime
import random
from .models import *
# Create your views here.

def HomePage(request):
    return HttpResponse("<h1>ji</h1>")

def aboutPage(request):
    a=2
    b=4
    sum = a + b

    customers = getCustomers()
    merchants = getMerchants()
    for merchant in merchants:
        print (merchant["name"])
    #print (makePayment(customers[0]["_id"],merchants[0],"A Huge Successful Hackathon",400,"10-11-2018","pending"))
    print (getPurchases(customers[0]["_id"]))
    """for customer in customers:
        print(customer["_id"],getPurchases(str(customer["_id"])))"""

    return HttpResponse(random.choices(getCustomers()))

def simulateSwipe(request):
    pass
