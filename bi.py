import requests #请求网页数据
from bs4 import BeautifulSoup #美味汤解析数据
import pandas as pd
import time
from tqdm import trange #获取爬取速度
def get_bilibili_url (start, end) :
    url_list = []
    date_list = [i for i in pd.date_range(start, end).strftime( '%Y-%m-%d' )]
    print(date_list)
    for date in date_list:
        url = f"https://api.bilibili.com/x/v2/dm/history?type=1&oid=141367679&date={date}"
        url_list.append(url)
    return url_list
def get_bilibili_danmu (url_list) :
    headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36" ,
        "cookie":"finger=158939783; _uuid=CC66B2AB-1EF3-4506-30B9-7821412D807059834infoc; buvid3=EA7E6036-EA63-4399-87B8-5397A272A38C143105infoc; LIVE_BUVID=AUTO6116001579759613; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(um|kJu)u|Y0J'uY||ul)|~Y; DedeUserID=382959668; DedeUserID__ckMd5=93f2a12d80e4bc88; SESSDATA=ba285785%2C1615711761%2C9a006*91; bili_jct=05182d13b7f0c4e800cd25e02b141397; sid=knwqbs48; PVID=1; bfe_id=5db70a86bd1cbe8a88817507134f7bb5"
    }
    file = open( "bilibili_danmu.txt", 'w',encoding='utf-8' )
    for i in trange(len(url_list)):
        url = url_list[i]
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text,features="html.parser")
        data = soup.find_all( "d" )

        danmu = [data[i].text for i in range(len(data))]
        for items in danmu:
            print(items)
            file.write(items)
            file.write( "\n" )
        time.sleep( 3 )
    file.close()

start = '9/24/2020' #设置爬取弹幕的起始日
end = '9/26/2020' #设置爬取弹幕的终止日
url_list = get_bilibili_url(start, end)
get_bilibili_danmu(url_list)
print(
"弹幕爬取完成"
)
