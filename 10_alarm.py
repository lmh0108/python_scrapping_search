import requests
import re
from bs4 import BeautifulSoup
import time
import numpy as np
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
url = "https://www.inven.co.kr/board/lostark/4811?p=1"
array1 = []
while True:
    kwd = input("키워드 입력(종료:0): ")
    if(kwd == str(0)):
        break
    array1.append(kwd)


while True:   
    ii = 0
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    w = soup.find_all("td",attrs={"class":"tit"})
    for i in range(len(array1)):
        for index, news in enumerate(w):
            tt = news.find("a").get_text().strip()
            lk=news.find("a")["href"]
            if(tt.find(array1[ii])!=-1 ):
                ii=ii+1
                print("{}".format(tt))
                print("  (링크 : {})".format(lk))
        ii=ii+1
    time.sleep(5)
