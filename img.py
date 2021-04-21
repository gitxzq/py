# -*- coding: utf-8 -*-
import requests
import time
import csv
import pandas as pd

# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用Cookie，跳过登陆操作
headers = {
  "Cookie": "appmsglist_action_3580804921=card; appmsglist_action_3882193727=card; ua_id=eJKOv7tJk7fgj9sNAAAAAAAoQXJ2WfWRwev_zLelO7U=; wxuin=15282907767496; openid2ticket_oGinM4msrqfxhjfofpH55WeOnyjI=; mm_lang=zh_CN; openid2ticket_ofVQBwwyCC40kZzjJ_BKeEz0uMzI=; openid2ticket_owYjD5ETlpHdeOlgE1WhSC0Pnr7k=; openid2ticket_oP5Nl5-YervHB25---RqsTAr9Pgw=; pgv_pvid=5493463424; ts_uid=3379108123; openid2ticket_o1whv6GVlvJFtXjB1Nj6iHvqzVsc=; tvfe_boss_uuid=b3f03b9d14c704d2; pac_uid=0_9453bfc8a823d; RK=SabkkJ16U6; ptcz=0fa6bb7c654ae16f21cfe48bbc76472d317113f4ba51134bac7b3b8da04c4c99; openid2ticket_oOb9u1TUN1RryljH268ude5rk_Ts=; rewardsn=; wxtokenkey=777; uuid=fd7892770ea327b6a5640a312b30acbc; rand_info=CAESIFzRRRyqH6EFl8CDl1hLq21uZhpVWgjQ3zbY36IeDQB4; slave_bizuin=3882193727; data_bizuin=3882193727; bizuin=3882193727; data_ticket=KWtozs4nI9akz8Y/PuHimP9v9rc3IZwXGTMdkTWdOny6WLPoaLKC6FdW55rlTm3c; slave_sid=bmZnZEZsbzZEZGtMbnEzdWFmQzF2Z2tMOVNlODBzc0hCUUMzSnoxWF9OejUzbEZxelpEUllHOEw5eTBHMWNfb2RacFRpM29lSDRRRVAxOWE0MURGd0FzNEpFMnE2WkZNOVM0MVlMRmpnWjZWa05JTnZkOVNacDNYWktPc00xSURpSTRNSHBOSERXRnM1bks4; slave_user=gh_605cdeee9022; xid=8d0de85bf336324d18f6b43f484a8f2c",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
}

data = {
    "token": "1051490797",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MjM5MDk3MTM3MQ==",
    "type": "9",
}

content_list = []
for i in range(30):
    data["begin"] = i*5
    time.sleep(5)
    # 使用get方法进行提交
    content_json = requests.get(url, headers=headers, params=data).json()
    # 返回了一个json，里面是每一页的数据
    for item in content_json["app_msg_list"]:    
    # 提取每页文章的标题及对应的url
        with open("D:\\weixin_img\\熊猫头表情包url.txt","a") as f:
            f.write(item["link"]+"\n")
            f.close()
    print(i)

print("保存成功")