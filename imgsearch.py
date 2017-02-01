import base64

def strToImgFile(img, filename):
    img_bytes = img.encode('ascii')
    decoded = base64.b64decode(img_bytes)
    f = open(filename, 'wb')
    f.write(decoded)
    f.close()
