import pymysql
import sys
import requests
import threading
from bs4 import BeautifulSoup

celeb_list = ['송중기', '러블리즈', '아이오아이']

time_list = [];
user_list = []
comment_list = [];
url_list = [];

def climber_crawler(celeb):
   #max_pages
   # page = 1
   # while page <= max_pages:
        url = 'https://search.naver.com/search.naver?where=realtime&sm=tab_jum&ie=utf8&query=' + celeb
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        spans = soup.find_all('span', {'class': 'sub_time _timeinfo'})
        for span in spans:
            if span != None:
                time_list.append(span.get_text())

        #a tag, txt_link, sub_time
        a_tags = soup.find_all('a')
        for a in a_tags:
            a_class = a.get('class')
            if a_class != None and a_class[0] == 'rt_user':
                user_list.append(a.get_text())
            if a_class != None and a_class[0] == 'txt_link':
                comment_list.append(a.get_text())
                url_list.append(a.get('href'))

        for i in range(10):
            print(time_list[i], user_list[i], comment_list[i], url_list[i])
#def call_climber_crawler():
#    timer = threading.Timer(10, call_climber_crawler)
#    for celeb in celeb_list:
#        print("============== " + celeb +  "시작 ==================")
#        climber_crawler(celeb)
#        print('============== '+celeb+' 종료 ==================')
#    timer.start()

#call_climber_crawler()

climber_crawler('송중기')