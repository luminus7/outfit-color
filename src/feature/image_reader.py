import cv2


class ImageReader:
    def __init__(self):
        pass

    # please use ABSOLUTE path
    @staticmethod
    def read(image_path):
        return cv2.imread(image_path)
