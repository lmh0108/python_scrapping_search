import requests
import re
from bs4 import BeautifulSoup
def curl(j):
    ss = 1
    kwd = input("키워드 입력: ")
    for i in range(3):
        url = "https://www.hallym.ac.kr/hallym_univ/sub05/cP3/sCP1?nttId=0&bbsTyCode=BBST00&bbsAttrbCode=BBSA03&authFlag=N&pageIndex="+str(i+1)+"&category="+str(j)+"&searchType=0&searchWrd="
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
                ss = 0
    if(ss==1):
        print("검색결과 없음.")

mm = int(input("0:전체공지  1.학사/학적/휴복학  2.장학/등록/증명  3.일반공지  4.행사안내  5.취업/인턴쉽  6.코로나19  7.교외공지----->"))
if(mm==0):
    curl("")
 
elif(mm==1):
    curl(mm)

elif(mm==2):
    curl(mm)

elif(mm==3):
    curl(mm)

elif(mm==4):
    curl(mm)

elif(mm==5):
    curl(mm)

elif(mm==6):
    curl(10382)

elif(mm==7):
    curl(mm)

else:
    print("다시 입력(0~7)")