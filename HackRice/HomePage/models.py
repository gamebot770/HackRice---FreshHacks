from django.db import models
import requests
import json
# Create your models here.

class Customer():
    def __init__(self):
        
        id= "",
        type= "",
        nickname= "",
        rewards= 0,
        balance= 0,
        account_number= "",
        customer_id= ""


def getCustomers():
    url = "http://api.reimaginebanking.com/accounts?key=a88246e847558936dbafc257d51fea7b"
    customers = requests.get(url)
    customerDictionary = customers.json()
    return customerDictionary

def getPurchases(id):
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key=a88246e847558936dbafc257d51fea7b".format(id)
    payments = requests.get(url)
    return payments.json()