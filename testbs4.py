# coding=utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# html=urlopen("http://www.pythonscraping.com/pages/page3.html")
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsobj=BeautifulSoup(html,features="html.parser")
# for child in bsobj.find('table',{'id':'giftList'}).children:
# for child in bsobj.find('table',{'id':'giftList'}).descendants:
#     print(child)

# for sibling in bsobj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)

# imgsurl=bsobj.find_all('img',{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
# for img in imgsurl:
#     print(img["src"])


# imgsurl=bsobj.select('img')
# for img in imgsurl:
#     print(img.attrs["src"])

# imgsurl=bsobj.find_all(lambda tag:len(tag.attrs)==2)
# print(imgsurl)

for link in bsobj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])





