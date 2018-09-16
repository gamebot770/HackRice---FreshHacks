from django.db import models
import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create your models here.

class Account(models.Model):

    id = models.CharField(max_length=24,primary_key=True)
    type = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100)
    rewards = models.IntegerField()
    balance = models.FloatField()
    account_number = models.CharField(max_length=24)
    customer_id = models.CharField(max_length=24)

    def update(self):
        accountUpdator = getAccount(self.id)
        self.type = accountUpdator["type"]
        self.nickname = accountUpdator["nickname"]
        self.rewards = accountUpdator["rewards"]
        self.balance = accountUpdator["balance"]
        self.account_number = accountUpdator["account_number"]
        self.customer_id = accountUpdator["customer_id"]
        return self.getNewPayments()

    def getNewPayments(self):
        loggedPayments = self.payments.all()
        currentPayments = getPayments(self.id)
        currentPayments = reversed(currentPayments)
        newPayments = []

        for payment in currentPayments:
            if payment in loggedPayments:
                return newPayments
            else:
                newPayments.append(payment)
                self.payments.add(payment)

class Payment(models.Model):
    account = models.ManyToManyField(Account)
    id = models.CharField(max_length=24,primary_key=True)
    type = models.CharField(max_length=24)
    merchant_id = models.CharField(max_length=100)
    payer_id = models.CharField(max_length=24)
    purchase_date = models.DateField()
    amount = models.FloatField()
    status = models.CharField(max_length=25)
    medium = models.FloatField()
    description = models.CharField(max_length=400)

def getCustomer(id):
    url = "http://api.reimaginebanking.com/customers/{}?key=a88246e847558936dbafc257d51fea7b".format(id)
    customer = requests.get(url).json()
    try:
        if customer["code"]=="404":
            return -1
    except:
        pass
    return customer

def getCustomer(id):
    url = "http://api.reimaginebanking.com/customers/{}?key=a88246e847558936dbafc257d51fea7b".format(id)
    customer = requests.get(url).json()
    try:
        if customer["code"]=="404":
            return -1
    except:
        pass
    return customer

def getCustomers():
    url = "http://api.reimaginebanking.com/customers?key=a88246e847558936dbafc257d51fea7b"
    customers = requests.get(url)
    customerDictionary = customers.json()
    return customerDictionary

def getCustomer(id):
    url = "http://api.reimaginebanking.com/customers/{}?key=a88246e847558936dbafc257d51fea7b".format(id)
    customer = requests.get(url).json()
    try:
        if customer["code"]=="404":
            return -1
    except:
        pass
    return customer

def getAccount(id):
    url = "http://api.reimaginebanking.com/accounts/{}?key=a88246e847558936dbafc257d51fea7b".format(id)
    account = requests.get(url)
    return account.json()

def getAccounts(id):
    url = "http://api.reimaginebanking.com/customers/{}/accounts?key=a88246e847558936dbafc257d51fea7b".format(id)
    accounts = requests.get(url).json()
    return accounts


def getPurchases(id):
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key=a88246e847558936dbafc257d51fea7b".format(id)
    payments = requests.get(url)
    return payments.json()

def getNewPurchases(id):
    allPurchases = getPurchases()
    allPurchases = reversed(allPurchases)
    #Load all purchases from the database
    #Loop backward until a marked record is found. If a payment is not then add it to the new list

def getMerchants():
    url = "http://api.reimaginebanking.com/merchants?key=a88246e847558936dbafc257d51fea7b"
    merchants = requests.get(url)
    return merchants.json()


def makePayment(customerID, merchant, description, amount, purchaseDate, status):
    paymentInfo = {
        "merchant_id": merchant["_id"],
        "medium": "balance",
        "purchase_date": purchaseDate,
        "amount": amount,
        "status": status,
        "description": description
    }
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key=a88246e847558936dbafc257d51fea7b".format(
        customerID)

    return requests.post(url, json.dumps(paymentInfo), headers={'content-type': 'application/json'})


def getPayments(accountID):
    url = "http://api.reimaginebanking.com/purchases/{}?key=a88246e847558936dbafc257d51fea7b".format(accountID)
    return requests.get(url).json()


def send_text(number, carrier, url):
    carrier_list= {"AT&T":"txt.att.net","T-Mobile":"tmomail.net","Verizon":"vtext.com", "Sprint":"messaging.sprintpcs.com",
                "Virgin Mobile":"vmobl.com","Tracfone":"mmst5.tracfone.com","Metro PCS":"mymetropcs.com",
                "Boost Mobile":"sms.myboostmobile.com","Cricket":"sms.cricketwireless.net","Republic Wireless":"text.republicwireless.com",
                "Google Fi":"msg.fi.google.com","U.S. Cellular":"email.uscc.net","Ting":"message.ting.com",
                "Consumer Cellular":"mailmymobile.net","C-Spire":"cspire1.com","PagePlus":"ytext.com"}

    message = MIMEMultipart()
    message['From'] = "expenditureender@gmail.com"
    message['To'] = str(number) + "@" + carrier_list[carrier]

    text = ("From: %s\r\nTo: %s\r\nSubject: \r\n\r\n"
            % (message['From'], ", ".join(message['To'])))
    text += "Mark your purchase here: " + url + "\r\n"

    message.attach(MIMEText(text.encode("utf-8"), "plain", "utf-8"))

    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login(message["From"], "kvgiaowqxzwbhfku")

    server.sendmail(message["From"], [message["To"]], text)