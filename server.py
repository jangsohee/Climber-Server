import thriftpy
oil_thrift = thriftpy.load("oil.thrift", module_name="oil_thrift")

from thriftpy.rpc import make_server

class OilHandler:
    def __init__(self):
        self.img_title = 0
        self.log = {}

    def ping(self):
        print("ping()")

    def imgSearch(self, img):
        img_file = open(self.get_img_title(), "w")
        #img_file.write(base64.b64decode(img))
        img_file.close()
        print("Image Search : image saved")

        similar = oil_thrift.SimilarImg("http://image.hankookilbo.com/i.aspx?Guid=5f5962508457411cb1882a0747acb9a0&Month=201603&size=640","http://m.naver.com")
        page = oil_thrift.MatchingPage("title", "http://image.hankookilbo.com/i.aspx?Guid=5f5962508457411cb1882a0747acb9a0&Month=201603&size=640", "http://m.naver.com", "content")

        result = oil_thrift.ImgSearchResult()
        print("Image Search : gen result")
        result.guess = "와왕 최유정 직찍"
        result.imgs = [similar, similar, similar, similar, similar]
        print("Image Search : fill imgs")
        result.pages = [page, page, page, page, page]
        print("Image Search : fill pages")

        print("Image Search : return result")
        return result

    def get_img_title(self):
        self.img_title += 1
        return repr(self.img_title)+".bmp"

server = make_server(oil_thrift.Oil, OilHandler(), '0.0.0.0', 9090)
print("starting oil server...")
server.serve()
print("done")
