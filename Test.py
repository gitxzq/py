# coding=utf-8

# import requests
# import json
# import random

# i=0
# while i<5:
#     url = "http://192.168.0.200:916/Goods/ProductItemAdd"
#     headers={'Cookie': '.ITC.Authentication=CfDJ8JqtIViTXxFMn_EUTKDTo5xzUDn1qcXVh2hEOh1j_WMzjJh8nrATOQh-HQTjVmkoS9DwqrthUfnsVuwpA5PVe5suY7e_RNXZPVMSQYxUetJq2BsUw9HTFB9Stu4EYt1l_tUKBUr9lPtUOzTA4ykm4-Pb9wwR2OdUlx-Hdl39nPGtyUWsiQuqd6d9GmnZUmy6vf5OtYIeKec59aBa6EwCJbk-YtM-IKZ6BtrwaPVM1KPpn6fOOUptjo8vSFsglLPbLCG0lYPh8pPe4U2XUDOBgOitmstsb_a95mv0rNA-RWRUpTF2-MMQ1AA1Z-LiKWcd6dWdkvLgd8nK1fd9l_t7BM4; .Pocket.Authentication=CfDJ8ETjeJhAh7ZFtGmyqQugSJjpFq5Kg9bO7K-ZsQRaCMNJKrLXQqViV6n9kG6njd8kMshQEHwgbsT84ucwWZePK6lKun3_dMdf6e615XAshrNTqDd_CgxwuWGe7T-ajEbPrz2Z32UeOh8Q0JN959dzosuLoKBUtAV5JOEhoW7iHLqDCzFgJFEBxOMcLPfNcX8DPQ1CQAwM00bHSmVVFDTueGedBAnsktb-F4c0PEZ05FqWYkVRJOsIPKo3EkgDx7ikOG3l0HkjVRoKMjPG2xRaYDhHg3sSVx7mab-3BPjNnR9-33X1U6DMRvrJnkFo3jg3hSYi_dxg9S7lCHoJsh3l6YWZMiDD7BKoBbxk8ExRCtRGt95iW8ShOLE1Pg0o1erJ-A; .Pocket.Admin=4F14F002-7BFD-4E97-9CB3-65DF2C44EF88; pgv_pvid=9032371880; __qc_wId=801; zentaosid=blmeu85k3ac2j3tnf2rqos11n4'}
#     productid=random.randint(0,7)
#     stock=random.randint(100,200)
#     date = {
#         "CreatedTime": "2021-02-03 00:00",
#         "EndTime": "2021-02-28",
#         "ProductId": productid,
#         "Stock": stock
#     }

#     response = requests.post(url, json=date,headers=headers)
#     text = response.text
#     i+=1R
#     print(text)

import hashlib

a='1019999.00'
b='955FE39D'

# str="fbf6446bda2be7a3"
str=a+b
m=hashlib.sha1(str.encode('utf-8'))

print('sha1=%s'%m.hexdigest().upper())

# from itertools import permutations
# L=list(permutations('12345'))
# for i in L:
#     for j in i:
#         print('-'.join(i))


# a='{"body":{"contentType":0,"content":"https://testgateway.shineupay.com/cashier/newdesk?id=20210201AAXEPROLN2805196","transactionId":"20210201AAXEPROLN2805196"},"status":0,"merchantId":"AAWK1GCDH1Q86386","timestamp":"1612171484464"}'
# b='|e004f3f1c9bf45ff8f2b7e057ec17f0f'
# str=a+b

# m=hashlib.md5(str.encode('utf-8'))
# print('sha1=%s'%m.hexdigest().lower())