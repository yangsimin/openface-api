import urllib
import numpy as np
import cv2


class ImageHelper:
    def __init__(self, logger):
        self.logger = logger

    def get_rgb_img_from_url_path(self, imgPath):
        self.logger.info("Calling get_rgb_img_from_url_path method")
        req = urllib.urlopen(imgPath)
        self.logger.info("After urllib.urlopen(imgPath)")
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        self.logger.info("After np.asarray")
        bgrImg = cv2.imdecode(arr, -1)  # 'load it as it is'
        self.logger.info("After cv2.imdecode")
        if bgrImg is None:
            self.logger.info("Unable to load image: %s" % imgPath)
            raise Exception("Unable to load image: %s" % imgPath)
        rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
        self.logger.info("After cv2.cvtColor")
        self.logger.info("End get_rgb_img_from_url_path method")
        return rgbImg

    def get_rgb_img_from_req_file(self, img):
        self.logger.info("Calling get_rgb_img_from_req_file method")
        bgrImg = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.CV_LOAD_IMAGE_UNCHANGED)
        self.logger.info("End cv2.imdecode..")
        if bgrImg is None:
            self.logger.info("Unable to load image from request body")
            raise Exception("Unable to load image from request body")
        rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
        self.logger.info("After cv2.cvtColor")
        self.logger.info("End get_rgb_img_from_req_file method")
        return rgbImg

    def get_rgb_img_from_base64(self, base64img):
        self.logger.info("End get_rgb_img_from_base64 method")
        nparr = np.fromstring(base64img.decode('base64'), np.uint8)
        bgrImg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        self.logger.info("End cv2.imdecode..")
        if bgrImg is None:
            self.logger.info("Unable to load image from request body")
            raise Exception("Unable to load image from request body")
        rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
        self.logger.info("After cv2.cvtColor")
        self.logger.info("End get_rgb_img_from_base64 method")
        return rgbImg

    def get_rgb_img_from_path(self, imgPath):
        self.logger.info("End get_rgb_img_from_path method")
        bgrImg = cv2.imread(imgPath)
        if bgrImg is None:
            raise Exception("Unable to load image: {}".format(imgPath))

        rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
        self.logger.info("End cv2.cvtColor..")
        self.logger.info("End End get_rgb_img_from_path method")
        return rgbImg
