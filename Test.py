# coding=utf-8

import requests
import json

date = {
    "username": 13632498945,
    "code": 1452,
}
url = "http://192.168.0.200:821/account/loginorregister"
response = requests.post(url, data=date)
text = response.text
jsonobj = json.loads(text)
print(jsonobj)

