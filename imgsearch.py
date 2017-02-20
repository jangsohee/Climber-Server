import base64
import os

def save_img(img, filename):
    img_bytes = img.encode('ascii')
    decoded = base64.b64decode(img_bytes)
    f = open(filename, 'wb')
    f.write(decoded)
    f.close()

def remove_img(filename):
    os.remove(filename)

def make_url(filename):
    search_url = 'http://www.google.co.kr/searchbyimage?image_url='
    img_url = 'oil.kkyung.com/imgs/' + filename
    url = search_url + img_url
    return url
