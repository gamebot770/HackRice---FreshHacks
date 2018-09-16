from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phoneNum = models.CharField(max_length=11)
    carrier = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    amount = models.FloatField()
    allocation = models.FloatField()


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
