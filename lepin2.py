'''
@Author: Never
@Date: 2020-06-13 11:02:05
@Description: 
@LastEditTime: 2020-06-18 18:59:45
@LastEditors: Never
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 19:47
# @Author  : Shark
# @Site    : 
# @File    : lepin1.py
# @Software: PyCharm


import csv
import requests
import json
with open('C:\\Users\\Administrator\\Desktop\\user.csv','rt') as myfile:
    lines=csv.reader(myfile)
    for memberid,test in lines:
        # print(memberid)
        # print(type(memberid))
        with open(r'F:\shop.h5\MemberId.json', 'w') as m:
            m.write(memberid)

        # date={
        #     "buynum": 1,
        #     "productid": "216930"
        # }
        #
        # url = "http://192.168.0.200:818/order/buyitnow"
        # response = requests.post(url,data=date)
        # text=response.text
        # jsonobj=json.loads(text)
        #
        # if jsonobj['success']==200:
        #     url="http://192.168.0.200:818/order/addorder"
        #     data={"TwoPersonChipNo": "",
        #             "mobileNo": "13632498944",
        #             "orderType": 0,
        #             "packs": {"216930":-1},
        #             "payPass": "",
        #             "remark": "{}",
        #             "shoppingBalance": 1,
        #             "useBalance": 0.02}
        #
        #     response=requests.post(url,data=data)
        #     text=response.text
        #     jsonobj=json.loads(text)
        #     print(jsonobj)
        # else:
        #     print(jsonobj)
        #     break



