import imutils
import cv2

from os import path


class PedestrianDetector:
    def __init__(self, image):
        self.__image = image
        self.__hog = cv2.HOGDescriptor()
        self.__hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self.__resize()

    def __resize(self):
        # shape: rsize(height), csize(width)
        imutils.resize(self.__image, width=min(400, self.__image.shape[1]))

    def catch_regions(self):
        (self.__regions, _) = self.__hog.detectMultiScale(self.__image,
                                                          winStride=(4, 4),
                                                          padding=(4, 4),
                                                          scale=1.05)
        return self.__regions
