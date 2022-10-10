import requests
import re
from bs4 import BeautifulSoup



url = "https://www.hallym.ac.kr/hallym_univ/sub05/cP3/sCP1?nttId=0&bbsTyCode=BBST00&bbsAttrbCode=BBSA03&authFlag=N&pageIndex=1&searchType=0&searchWrd="
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

kwd = input("키워드 입력: ")
w = soup.find("ul",attrs={"class":"tbl-body"}).find_all("li")
for index, news in enumerate(w):
    tt = news.find("a").get_text().strip()
    lk=news.find("a")["href"]
    res2 = requests.get(lk)
    soup2 = BeautifulSoup(res2.text, "lxml")
    w1 = soup2.select_one('.boardview-con').get_text()
    if((w1.find(kwd)!=-1)):
        print("{}".format(tt))
        print("  (링크 : {})".format(lk))