# coding=utf-8

import requests


def baidu_search(query, region, tag):
    url = 'http://api.map.baidu.com/place_abroad/v1/search?'
    output = 'json'
    ak = 'qzes9D1Lb4aqdAeMFoV5S0z5VCgCr9yo'
    uri = url + 'query=' + query + '&region=' + region + '&tag=' + tag + '&output=' + output + '&ak=' + ak
    # print(uri)
    r = requests.get(uri)
    response_dict = r.json()
    print(response_dict)
    results = response_dict["results"]
    print(results)
    for adr in results:
        name = adr['name']
        if 'telephone' in adr:
            telephone = adr['telephone']
            print('名称：' + name)
            print('电话：' + telephone)


baidu_search('Bindra park', '印度新德里', '超市')


