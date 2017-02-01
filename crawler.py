import requests
from bs4 import BeautifulSoup


def climber_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://search.naver.com/search.naver?where=realtime&sm=tab_jum&ie=utf8&query=송중기'
        source_code = requests.get(url, allow_redirects=False)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html.parser')
        for comments in soup.findAll('a', {'class': 'txt_link'}):
            print(comments.get_text())
        for comments in soup.findAll('span', {'class': 'cmmt _twitter'}):
            print(comments.get_text())
        page += 1
climber_crawler(1)
