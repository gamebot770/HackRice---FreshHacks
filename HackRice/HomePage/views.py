from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
# Create your views here.

def HomePage(request):
    return HttpResponse("<h1>ji</h1>")

def aboutPage(request):
    a=2
    b=4
    sum = a + b
    return render(request,"HomePage/template-pages/index.html",{"sum":sum})