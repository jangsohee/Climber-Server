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
