import requests
from json.decoder import JSONDecoder
import json
import base64, requests, sys
from requests.auth import HTTPBasicAuth
import os

auth_token="0da6621d068ea484d8352cc2cc76675e6b63492e"
#Update QR code 
url = "https://api.beaconstac.com/api/2.0/qrcodes/527917/"
headers = {
    'Authorization': 'Token 0da6621d068ea484d8352cc2cc76675e6b63492e'
} #space added
payload = {
    "campaign": {
        "content_type": 1,
        "custom_url": "https://google.com"
    }
}          
response = requests.request("PUT", url, headers=headers, data=payload)
#response = requests.put(url, headers=headers, data={"campaign":{"name":"http://www.google.com"}})
print(response.text)
print(response)

