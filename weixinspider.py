import requests
from bs4 import BeautifulSoup
import re
import os
import io
import imghdr
import time

#获取网页信息
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

#解析网页，获取所有图片url
def getimgURL(html):
    soup = BeautifulSoup(html , "html.parser")
    adlist=[]
    for i in soup.find_all("img"):
        try:
            ad= re.findall(r'.*src="(.*?)?" .*',str(i))
            if ad :
                adlist.append(ad)
        except:
            continue
    return adlist

#新建文件夹pic，下载并保存爬取的图片信息
def download(adlist,url,j):
    #注意更改文件目录

    root="D:\\weixin_img\\熊猫头表情包\\"+str(j)+"\\"
    for i in range(len(adlist)-1):
        if not os.path.exists(root):
            os.mkdir(root)
        # if not os.path.exists(path):
        r=requests.get(adlist[i][0])
        image=r.content
        image_b=io.BytesIO(image).read()
        gs=imghdr.what(None,h=image_b)
        path=root+str(i)+"."+gs        
        with open(path,'wb') as f:
            f.write(image)
            f.close()
        print(i)
    print("第 %s 篇" %(j))

def main():
    with open("D:\\weixin_img\\熊猫头表情包url.txt","r") as f:
        j=16
        for url in f.readlines():
            html=getHTMLText(url)
            list=getimgURL(html)            
            download(list,url,j)
            j+=1
            time.sleep(1)
main()