import requests
from access_token import get_access_token
from config import Config
from encode_pass import get_password
from time_formart import get_time_stamp

BusinessShortCode=Config["BUSINESS_SHORT_CODE"]
shortcode=Config["Lipa Na Mpesa Online Shortcode"]
phone_number=Config["PHONE_NUMBER"]
timestamp=get_time_stamp()
password=get_password(timestamp)
access_token = get_access_token()

def lipa_na_mpesa():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": shortcode,
    "Password": password,
    "Timestamp": timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 2,
    "PartyA": phone_number,
    "PartyB": shortcode,
    "PhoneNumber": phone_number,
    "CallBackURL": "https://pizzaorder.com/callback",
    "AccountReference": "01 ",
    "TransactionDesc": "orderprize "
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

if __name__=="__main__":
    lipa_na_mpesa()