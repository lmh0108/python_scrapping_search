from pickle import TRUE
import requests
import re
from bs4 import BeautifulSoup

def title(j,l,k):
    ss = 1 
    for i in range(3):
        url = "https://www.hallym.ac.kr/hallym_univ/sub05/cP3/sCP1?nttId=0&bbsTyCode=BBST00&bbsAttrbCode=BBSA03&authFlag=N&pageIndex="+str(i+1)+"&category="+str(j)+"&searchType=0&searchWrd="
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        w = soup.find("ul",attrs={"class":"tbl-body"}).find_all("li")
        for index, news in enumerate(w):
            tt = news.find("a").get_text().strip()
            lk=news.find("a")["href"]
            res2 = requests.get(lk)
            soup2 = BeautifulSoup(res2.text, "lxml")
            w1 = soup2.select_one('.boardview-con').get_text()
            if(l == 1):
                if(tt.find(k)!=-1):
                    print(str(i+1)+"페이지")
                    print("{}".format(tt))
                    print("  (링크 : {})".format(lk))
                    ss = 0
            elif(l == 2):
                if((w1.find(k)!=-1)):
                    print(str(i+1)+"페이지")
                    print("{}".format(tt))
                    print("  (링크 : {})".format(lk))
                    ss = 0
            elif(l == 3):
                if((tt.find(k)!=-1) or (w1.find(k)!=-1)):
                    print(str(i+1)+"페이지")
                    print("{}".format(tt))
                    print("  (링크 : {})".format(lk))
                    ss = 0
    if(ss==1):
        print("검색결과 없음.")
mm = int(input("0:전체공지  1.학사/학적/휴복학  2.장학/등록/증명  3.일반공지  4.행사안내  5.취업/인턴쉽  6.코로나19  7.교외공지----->"))
slt = int(input("1:제목  2:내용  3:제목+내용--->"))
kwd = input("키워드 입력: ")
bol = not(0<slt<4)
if(bol):
    print("다시입력(1~3)")

if(mm==0):
    title("",slt,kwd)

elif(mm==1):
    title(mm,slt,kwd)

elif(mm==2):
    title(mm,slt,kwd)

elif(mm==3):
    title(mm,slt,kwd)

elif(mm==4):
    title(mm,slt,kwd)

elif(mm==5):
    title(mm,slt,kwd)

elif(mm==6):
    title(10382,slt,kwd)


elif(mm==7):
    title(mm,slt,kwd)

else:
    print("다시 입력(0~7)")