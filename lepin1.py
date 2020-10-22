'''
@Author: Never
@Date: 2020-06-13 11:02:05
@Description: 
@LastEditTime: 2020-07-14 15:20:19
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
import random
import time

start =time.time()
print('程序开始时间：%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start))))

WinStatuslist=[]
i=0
with open('C:\\Users\\lhx\\Desktop\\user1.csv','rt') as myfile:
    lines=csv.reader(myfile)
    for memberid,addid in lines:
        with open(r'\\192.168.0.200\shop.h5\MemberId.json', 'w') as m:
            m.write(memberid)
        t=0 
        while t<20:
            date={
            "productid":216869,
            "lpTimes":1,
            "addressid":addid,
            "isPay":'true',
            "useBalance":10.9,
            }
            
            url = "http://192.168.0.200:818/order/ActivityOrderConfirm"
            response = requests.post(url,data=date)
            text=response.text
            jsonobj=json.loads(text)

            
            if jsonobj['success']==200:
                totext=jsonobj['data']['OrderIdList']
                url="http://192.168.0.200:818/HappyOrder/ForthWithOrder"       
                data={"happyOrderId":totext,
                "chooseNumber":random.randint(0,9)}

                response=requests.post(url,data=data)
                text=response.text
                jsonobj=json.loads(text)

                totext=jsonobj['data']['WinStatus']
                WinStatuslist.append(totext)
            else:
                print(jsonobj)
                break
            t+=1
            # time.sleep(1)
        i+=1
        print(i)

m=0
print(WinStatuslist)
for j in WinStatuslist:
    if j==1:
        m+=1
i=20*i
print("订单数：%s"%i)
print("中奖次数：%s"%m)
s=m/i*100
print('中奖概率：{:.2f}%'.format(s))
end =time.time()
print('程序结束时间：%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end))))
print("循环运行时间:%.2f秒"%(end-start))
        