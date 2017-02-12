import requests
import pymysql
import sys
from bs4 import BeautifulSoup

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

climber_crawler('송중기')
