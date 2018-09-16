from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from HomePage.models import *
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phoneNum = models.CharField(max_length=11)
    carrier = models.CharField(max_length=24)
    id = models.CharField(max_length=24,primary_key=True)
    address = models.CharField(max_length=4000)


class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    amount = models.FloatField()
    allocation = models.FloatField()

def updateCustomerData(user):
    customer = getCustomer(user.userprofile.id)
    if customer != -1:
        user.id = customer["_id"]
        user.first_name = customer["first_name"]
        user.last_name = customer["last_name"]
        user.userprofile.address = customer["address"]
        user.save()






@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.save()
    except:
        pass
