from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from .models import *
import datetime
# Create your views here.

def HomePage(request):

    customers = getCustomers()
    customer = getCustomer(customers[1]["_id"])
    account = getAccounts(customer["_id"])
    return HttpResponse(account)

def baseTemplate(request):
    return render(request,"HomePage/baseTemplate.html",{})

def aboutPage(request):
    a=2
    b=4
    sum = a + b
    return render(request,"HomePage/home.html",{"sum":sum})

def login(request):
    return render(request, "HomePage/login.html", {})

def categorySelection(request):
    return render(request,"HomePage/categorySelection.html",{})

def transactionUpdate(request):
    return render(request,"HomePage/transactionUpdate.html",{})

def signUp(request):
    print(reverse('signUp'))
    return render(request,"HomePage/signUp.html",{})

def dashboard(request):
    return render(request,"HomePage/dashboard.html",{})

def viewAccounts(request):

    account = getAccount(request.user.userprofile.id)
    accId = account.id
    accType = account.type
    accNickname = account.nickname
    accRewards = account.rewards
    accBalance = account.balance
    accNumber = account.account_number
    customerId = account.customer_id

    return render(request,"HomePage/viewAccounts.html",{"accId":accId, "accType":accType, "accNickname":accNickname,
                    "accRewards":accRewards, "accBalance":accBalance, "accNumber":accNumber, "customerId":customerId})