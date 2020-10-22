'''
@Author: Never
@Date: 2020-06-13 11:41:52
@Description: 
LastEditTime: 2020-08-12 10:29:32
LastEditors: Never
'''
import requests
import json
import random
import time
start =time.time()
print('程序开始时间：%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start))))
WinStatuslist=[]
i=0
while i<100:
    
    date={
    "productid":228604,
    "lpTimes":1,
    "addressid":271164,
    "isPay":'true',
    "useBalance":61,
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
        i+=1
        print(i)
        
    else:
        print(jsonobj)
        continue
    
    
print(WinStatuslist)
m=0
for j in WinStatuslist:
    if j==1:
        m+=1
s=m/i*100
end =time.time()
print("订单数：%s"%i)
print("中奖次数：%s"%m)
print('中奖概率：{:.2f}%'.format(s))
print('程序结束时间：%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end))))

print("循环运行时间:%.2f秒"%(end-start))