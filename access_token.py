import os
import requests
from requests.auth import HTTPBasicAuth

def get_access_token():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    response=r.json()
    myaccesstoken=response["access_token"]
    print(myaccesstoken)
    return myaccesstoken


get_access_token()