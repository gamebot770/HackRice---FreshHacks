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
