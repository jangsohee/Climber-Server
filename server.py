import thriftpy
oil_thrift = thriftpy.load("oil.thrift", module_name="oil_thrift")

from thriftpy.rpc import make_server
import imgsearch

class OilHandler:
    def __init__(self):
        self.img_title = 0
        self.log = {}

    def ping(self):
        print("ping()")

    def imgSearch(self, img):
        imgsearch.remove_img(self.get_prev_filename())
        print("Image Search : previous image deleted")

        filename = self.get_new_filename()
        imgsearch.save_img(img, filename)
        print("Image Search : image saved")

        imgsearch.make_url(filename)
        print("Image Search : url generated")

        return result

    def get_new_filename(self):
        self.img_title += 1
        return "~/www/imgs/" + repr(self.img_title) + ".bmp"

    def get_prev_filename(self):
        return "~/www/imgs/" + repr(self.img_title) + ".bmp"

server = make_server(oil_thrift.Oil, OilHandler(), '0.0.0.0', 9090)
print("starting oil server...")
server.serve()
print("done")
