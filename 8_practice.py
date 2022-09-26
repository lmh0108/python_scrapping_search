import requests
import re
from bs4 import BeautifulSoup

kwd = input("키워드 입력: ")
for i in range(3):
    url = "https://www.hallym.ac.kr/hallym_univ/sub05/cP3/sCP1?nttId=0&bbsTyCode=BBST00&bbsAttrbCode=BBSA03&authFlag=N&pageIndex="+str(i+1)+"&searchType=0&searchWrd="
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    w = soup.find("ul",attrs={"class":"tbl-body"}).find_all("li")
    for index, news in enumerate(w):
        tt = news.find("a").get_text().strip()
        lk=news.find("a")["href"]
        if(tt.find(kwd)!=-1):
            print(str(i+1)+"페이지")
            print("{}".format(tt))
            print("  (링크 : {})".format(lk))
