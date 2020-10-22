from bs4 import BeautifulSoup
from urllib.request import urlopen

html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsobj=BeautifulSoup(html)
namelist=bsobj.find_all('span',{'class','green'})
for name in namelist:
    print(name.get_text())