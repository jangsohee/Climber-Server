import pymysql
import sys
import requests
#import threading
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

celeb_list = ['송중기', '러블리즈', '아이오아이']

time_list = [];
user_list = []
comment_list = [];
url_list = [];

def convertTime(timeStr):
    now = datetime.now()
    strlen = len(timeStr)

    if strlen == 6:
        #00시간 전
        h = int(timeStr[0]+timeStr[1])
        timeGap = timedelta(hours=h)
        before = now - timeGap
        nDate = before.strftime('%Y-%m-%d %H:%M')
        return nDate
    elif strlen == 5:
        #00분 전 or 0시간 전
        if timeStr[2] == '분':
            #00분 전
            m = int(timeStr[0]+timeStr[1])
            timeGap = timedelta(minutes=m)
            before = now - timeGap
            nDate = before.strftime('%Y-%m-%d %H:%M')
            return nDate
        else:
            #0시간 전
            h = int(timeStr[0])
            timeGap = timedelta(hours=h)
            before = now - timeGap
            nDate = before.strftime('%Y-%m-%d %H:%M')
            return nDate
    elif strlen == 4:
        #0분 전, 0일 전
        if timeStr[2] == '분':
            #0분 전
            m = int(timeStr[0])
            timeGap = timedelta(minutes=m)
            before = now - timeGap
            nDate = before.strftime('%Y-%m-%d %H:%M')
            return nDate
        else:
            #0일 전
            d = int(timeStr[0])
            timeGap = timedelta(days=d)
            before = now - timeGap
            nDate = before.strftime('%Y-%m-%d %H:%M')
            return nDate

def climber_crawler(celeb):
   #max_pages
   # page = 1
   # while page <= max_pages:
        url = 'https://search.naver.com/search.naver?where=realtime&sm=tab_jum&ie=utf8&query=' + celeb
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        li_tags = soup.find_all('li')

        #글쓴이
        for li in li_tags:
            a_tags = li.find_all('a')
            for a in a_tags:
                a_class = a.get('class')
                if a_class != None and a_class[0] == 'rt_user':
                    user_string = a.get_text()
                    if user_string.find('@') == -1:
                        user_list.append(user_string)

        #시간
        spans = soup.find_all('span', {'class': 'sub_time _timeinfo'})
        for span in spans:
            if span != None:
                time_list.append(convertTime(span.get_text()))


        #댓글, 주소
        a_tags = soup.find_all('a')
        for a in a_tags:
            a_class = a.get('class')
            #if a_class != None and a_class[0] == 'rt_user':
                #user_string = a.get_text()
                #if user_string.find('@') == -1:
                    #user_list.append(user_string)
                    #print(user_string)
            if a_class != None and a_class[0] == 'txt_link':
                comment_list.append(a.get_text())
                url_list.append(a.get('href'))

        zero_chk = (len(time_list) + len(user_list) + len(comment_list) + len(url_list))
        if (len(time_list) == len(user_list) == len(comment_list) == len(url_list)) and zero_chk != 0:
            for i in range(len(time_list)):
                print(time_list[i], user_list[i], comment_list[i], url_list[i])

#def call_climber_crawler():
#    timer = threading.Timer(10, call_climber_crawler)
#    for celeb in celeb_list:
#        print("============== " + celeb +  "시작 ==================")
#        climber_crawler(celeb)
#        print('============== '+celeb+' 종료 ==================')
#    timer.start()

#call_climber_crawler()

climber_crawler('구혜선')
