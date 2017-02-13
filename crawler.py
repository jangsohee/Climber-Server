import requests
import threading
import sys
from bs4 import BeautifulSoup

celeb_list = ['송중기', '러블리즈', '아이오아이']

def climber_crawler(celeb):
   #max_pages
   # page = 1
   # while page <= max_pages:
        url = 'https://search.naver.com/search.naver?where=realtime&sm=tab_jum&ie=utf8&query=' + celeb
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #a tag, txt_link
        a_tags = soup.find_all('a')
        for a in a_tags:
            a_class = a.get('class')
            if a_class != None and a_class[0] == 'rt_user':
                user = a.get_text()
            if a_class != None and a_class[0] == 'txt_link':
                comment = a.get_text()
                url = a.get('href')
                print(user, comment, url)


def call_climber_crawler():
    timer = threading.Timer(10, call_climber_crawler)
    for celeb in celeb_list:
        print("============== " + celeb +  "시작 ==================")
        climber_crawler(celeb)
        print('============== '+celeb+' 종료 ==================')
    timer.start()

call_climber_crawler()
