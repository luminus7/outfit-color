from image_reader import ImageReader
from pedestrian_detector import PedestrianDetector
from clothes_color_detector import ClothesColorDetector
from os import path
if __name__=="__main__":
    pedestrian_image_path=f"{path.dirname(path.abspath(__file__))}\\images\\person_wearing_clothes.jpg"
    pedestrian_image=ImageReader.read(pedestrian_image_path)
    region_s=PedestrianDetector(pedestrian_image).return_region_images()
    for i, region in enumerate(region_s):
        clothes_color_s=ClothesColorDetector.detect_clothes_color(region)
        print(f"image #{i}")
        for k,clothes_color in enumerate(clothes_color_s):
            print(f"#{k}: {clothes_color}",end="  ")
        print("\n")