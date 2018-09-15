from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from firebase import firebase

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

def urlGenerator(request):
    ##firebase1 = firebase.FirebaseApplication('https://ricehakkrs.page.link', None)
    url = firebase.make_post_request("https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=AIzaSyDrL-q7Zz-Y1TzQp3mqLTiWPYNupvoxEuM",
                        {"longDynamicLink":"https://ricehakkrs.page.link/?link=https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        "suffix":"SHORT"})
    print(url)
    return HttpResponse(url)