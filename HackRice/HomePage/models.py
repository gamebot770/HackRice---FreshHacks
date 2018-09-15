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

def getMerchants():
    url = "http://api.reimaginebanking.com/merchants?key=a88246e847558936dbafc257d51fea7b"
    merchants = requests.get(url)
    return merchants.json()

def makePayment(customerID,merchant,description,amount,purchaseDate,status):

    paymentInfo = {
        "merchant_id": merchant["_id"],
        "medium": "balance",
        "purchase_date": purchaseDate,
        "amount": amount,
        "status": status,
        "description": description
    }
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key=a88246e847558936dbafc257d51fea7b".format(customerID)

    return requests.post(url,json.dumps(paymentInfo),headers={'content-type':'application/json'})

def getPayments(customerID):
    url = "http://api.reimaginebanking.com/purchases/{}?key=a88246e847558936dbafc257d51fea7b".format(customerID)
    return requests.get(url).json()