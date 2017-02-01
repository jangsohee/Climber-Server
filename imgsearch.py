import base64
import os
import requests

def save_img(img, filename):
    img_bytes = img.encode('ascii')
    decoded = base64.b64decode(img_bytes)
    f = open(filename, 'wb')
    f.write(decoded)
    f.close()

def remove_img(filename):
    os.remove(filename)

def img_search(filename):
    search_url = 'http://images.google.com/searchbyimage?site=search&image_url='
    img_url = 'oil.kkyung.com/imgs/' + filename
    url = search_url + img_url
    response = requests.get(url)
    response = requests.get(response.url)
    f = open('resp.txt', 'w')
    f.write(response.text)
    f.close()

img_search('a.jpg')
