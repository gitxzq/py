#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
driver = webdriver.Chrome(chrome_options=chrome_options)
i=0
file = open( "name1.txt", 'w',encoding='utf-8' )
while i<500:
    url = "https://fakenametool.net/fake-name-generator/en_IN?"
    driver.get(url)
    name=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]').text
    print(name)
    file.write(name)
    file.write( "\n" )
    time.sleep(1)  
    driver.refresh()
    i+=1
driver.close()
