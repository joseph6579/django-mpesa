import requests
from  datetime import datetime
from requests.auth import HTTPBasicAuth
import json
from base64 import b64encode

from django.conf import settings


if settings.MPESA_PRODUCTION:
    url = settings.MPESA_PROD_BASE_URL
else:
    url = settings.MPESA_SANDBOX_BASE_URL



consumer_key =  "H4WeAk4P8XW5dCyPPRnpvvxkiSLjSQiR" #"HiGPy6A7jtG9cZaHTkYfC9AQEwvsD0Bx"
consumer_secret = "qmxDmH1sFCaX5a6F" #"tFdqCUYI9jGiNfCu"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
Passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" #"d5496f55bb160764bd4e5732b85a7e42c17eeda11289e8f1e91a044684d1e8c7"
Shortcode = 174379


def get_token():
  r = requests.get(api_URL, auth=HTTPBasicAuth(settings.CONSUMER_KEY, settings.CONSUMER_SECRET))
  token = r.json()
  return(token["access_token"])


token = get_token()


def get_time():
  now = datetime.now()
  formatted_time = now.strftime("%Y%m%d%H%M%S")
  return formatted_time

githaa = get_time()
short = str(Shortcode)

def encoded_pass():
  githaa = get_time()
  pwd = (settings.SHORTCODE+Passkey+githaa).encode('utf-8')
  pwd_enc = b64encode(pwd).decode('ascii')
  return pwd_enc

pass_enc = encoded_pass()


def stk_push(phone_number, amount, acc_ref, trans_desc):
    access_token = token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": Shortcode,
    "Password": pass_enc,
    "Timestamp": githaa,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": phone_number,
    "PartyB":  settings.SHORTCODE,
    "PhoneNumber": phone_number,
    "CallBackURL": settings.CALLBACK_URL,
    "AccountReference": acc_ref,
    "TransactionDesc": trans_desc
    }

    response = requests.post(api_url, json = request, headers=headers)

    print(phone_number, amount, acc_ref, trans_desc)
    print (response.text)   
    return response.text 



if __name__ == "__main__":
    stk_push()
