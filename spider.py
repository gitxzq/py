from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
res = urlopen("http://www.baidu.com")
soup=BeautifulSoup(res,'lxml')
title=soup.find("title").text
print(title)