#coding=utf-8

import requests
import random

userid_list=[]
with open(r'C:\Users\Administrator\Desktop\userid.txt','r') as f:
    for line in f.readlines():
        userid_list.append(line)

for userid in userid_list:
    with open(r'E:\wwwroot\shop.h5\MemberId.json','w') as m:
        m.write(userid)
        
    number=random.randint(1,9)
    data = {
        "number":number
    }

    url='http://192.168.0.200:818/PusherActivity/BuyLuckCode'

    def send_request(url,data):
        rsp=requests.post(url=url,data=data)
        return rsp
    send_rsq=send_request(url,data)

    print(send_rsq.json())
