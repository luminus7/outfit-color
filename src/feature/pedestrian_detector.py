import imutils
import cv2


class PedestrianDetector:
    def __init__(self, image):
        self.__image = image
        self.__hog = cv2.HOGDescriptor()
        self.__hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self.__resize()
        self.__region_s = None

    def __resize(self):
        # shape: rsize(height), csize(width)
        imutils.resize(self.__image, width=min(400, self.__image.shape[1]))

    def catch_regions(self):
        (self.__region_s, _) = self.__hog.detectMultiScale(self.__image,
                                                           winStride=(4, 4),
                                                           padding=(4, 4),
                                                           scale=1.05)

        return self.__region_s
