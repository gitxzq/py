'''
@Author: Never
@Date: 2020-06-13 11:02:05
@Description: 
@LastEditTime: 2020-07-31 17:34:05
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
import time
import multiprocessing
import threading


start =time.time()
queue=multiprocessing.Queue(maxsize=0)
print('程序开始时间：%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start))))
with open('C:\\Users\\lhx\\Desktop\\拼多多商品1.csv','rt') as myfile:
    lines=csv.reader(myfile)
    for ProductId in lines:
        queue.put(ProductId)

class myThread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name=name
    def run(self):

        print("Starting " + self.name) 
        qu_pro(self.name)        
        print("Exiting " + self.name) 


def qu_pro(threadname):
    while True:
        if not queue.empty():
            date={
                "timeStamp":"1596187879",
                "Locat":{"LngLatStr":""},
                "ProductType":	15,
                "sign":"C3504BE69C5234ED8591738A481DF159",
                "imei":"66fb2285-6502-331a-87ee-4176def41780",
                "client":2,
                "ProductId":queue.get(),
                "ItemId":0,
                "version":"3.3.2",
                "versionCode":69,
                "token":"f46556bb-8dce-432d-a4f0-ba994557c1d0",
                "channelCode":"xiaomi"
            }
            url = "http://api1.huizhisuo.com/Product/GenProductUrl"
            response = requests.post(url,data=date)
            text=response.text
            print(text)
        else:
            break


thread1=myThread(1,"thread-1")
thread2=myThread(2,"thread-2")

thread1.start()
thread2.start()


end=time.time()
print('程序结束时间：%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end))))