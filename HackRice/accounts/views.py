from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from accounts.models import *
from HomePage.models import *
from django.shortcuts import redirect,HttpResponseRedirect,reverse

# Create your views here.
def signUp(request):
    if request.POST:
        print(request.POST)

        email = request.POST["email"]
        password = request.POST["confirm_password"]
        phoneNum = request.POST["phoneNumber"]
        carrier = request.POST["carrier"]

        user = User()
        user.username = request.POST["id"]
        user.set_password(password)
        user.email = email
        user.save()

        user.userprofile.phoneNum = phoneNum
        user.userprofile.carrier = carrier
        user.userprofile.save()

        if getCustomer(user.userprofile.id)!= -1:
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            addCustomer(User)
            return HttpResponseRedirect(reverse('dashboard'))

def signIn(request):
    if request.method == "POST":

        temp = User()
        temp.username = request.POST["username"]
        temp.password = request.POST["password"]

        user = authenticate(request,username=request.POST["username"],password=request.POST["password"])

        if user is not None:
            print(user)
            if user.is_active:
                login(request,user)
                updateCustomerData(user)
                print(getCustomer(request.user.userprofile.id))
                if getCustomer(request.user.userprofile.id) != -1:
                    return HttpResponseRedirect(reverse('dashboard'))
                else:
                    print("DONE!")
                    addCustomer(User)
                    return HttpResponseRedirect(reverse('dashboard'))

        return HttpResponseRedirect(reverse("login"))
