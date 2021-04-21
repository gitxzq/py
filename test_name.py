# coding=utf-8
import requests #请求网页数据
from bs4 import BeautifulSoup #美味汤解析数据
from lxml import etree
# import pandas as pd
import time
# from tqdm import trange #获取爬取速度

def xpath_parse_name(html):
    et_html = etree.HTML(html)
    # 查找所有class属性为hd的div标签下的a标签的第一个span标签
    urls = et_html.xpath("/html/body/div[2]/div/div[2]/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]")
    # movie_list = []
    # # 获取每个span的文本
    for each in urls:
        name = each.text.strip()
    # print(name)
    return name

def test_name() :
    headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36" ,
        "cookie":"finger=158939783; _uuid=CC66B2AB-1EF3-4506-30B9-7821412D807059834infoc; buvid3=EA7E6036-EA63-4399-87B8-5397A272A38C143105infoc; LIVE_BUVID=AUTO6116001579759613; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(um|kJu)u|Y0J'uY||ul)|~Y; DedeUserID=382959668; DedeUserID__ckMd5=93f2a12d80e4bc88; SESSDATA=ba285785%2C1615711761%2C9a006*91; bili_jct=05182d13b7f0c4e800cd25e02b141397; sid=knwqbs48; PVID=1; bfe_id=5db70a86bd1cbe8a88817507134f7bb5"
    }
    url = 'https://fakenametool.net/fake-name-generator/id_ID?'
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    print("状态码：",r.status_code)
    # if 200!=r.status_code:
    #     return None

    return xpath_parse_name(r.text)

    # danmu = [data[i].text for i in range(len(data))]
    # for items in danmu:
    #     print(items)
    #     file.write(items)
    #     file.write( "\n" )
    # time.sleep( 3 )
    # file.close()

# test_name()
file = open( "yinni_name.txt", 'w',encoding='utf-8' )
i=0
name_list=[]
while i<1000:
    name=test_name()
    print(name)
    file.write(name)
    file.write("\n")
    time.sleep(0.5)
    i+=1
file.close()
