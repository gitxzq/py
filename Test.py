# coding=utf-8

# import requests
# import json

# date = {
#     "username": 13632498945,
#     "code": 1452,
# }
# url = "http://192.168.0.200:821/account/loginorregister"
# response = requests.post(url, data=date)
# text = response.text
# jsonobj = json.loads(text)
# print(jsonobj)

# import hashlib

# a='10000.0000'
# b='98022E'

# str=a+b

# m=hashlib.sha1(str.encode('utf-8'))

# print('sha1=%s'%m.hexdigest().upper())


from itertools import permutations
L=list(permutations('12345'))
for i in L:
    for j in i:
        print('-'.join(i))