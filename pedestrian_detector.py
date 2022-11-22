import imutils
import cv2


class PedestrianDetector:
    def __init__(self, image):
        self.__image = image
        self.__hog = cv2.HOGDescriptor()
        self.__hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self.__resize()
        self.__region_s=None

    def __resize(self):
        # shape: rsize(height), csize(width)
        imutils.resize(self.__image, width=min(400, self.__image.shape[1]))

    def __catch_regions(self):
        (self.__region_s, _) = self.__hog.detectMultiScale(self.__image,
                                                           winStride=(4, 4),
                                                           padding=(4, 4),
                                                           scale=1.05)

    def return_region_images(self):
        self.__catch_regions()
        region_image_s = []
        for (x, y, w, h) in self.__region_s:
            region_image = self.__image[y:y + h, x:x + w]
            region_image_s.append(region_image)
        return region_image_s
