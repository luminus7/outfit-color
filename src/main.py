import sys
import cv2

from feature.clothes_color_detector import ClothesColorDetector
from feature.clothes_color_presenter import ClothesColorPresenter
from feature.frame_extractor import extract_frame
from feature.pedestrian_detector import PedestrianDetector

if __name__ == "__main__":
    """ If you are using Windows + Vscode, enable comments in below ..."""
    # if (len(sys.argv)-1) != 1:
    #     print("Please feed the file path you want to run")
    # video_path = sys.argv[1]
    # print(video_path)
    """                        Windows + Vscode                        """
    """ and add...
                "args": ["\\\\videos\\\\1-person_walking.mp4"],
        to the 'launch.json' file.
        you can make the file easily by 'Run and Debug' sidebar (ctrl+shift+D)
    """

    video_path = "videos\\1-person_walking.mp4"
    frame_s = extract_frame(video_path)
    delay = int(1000 / cv2.CAP_PROP_FPS)
    for frame in frame_s:
        region_s = PedestrianDetector(frame).catch_regions()
        presenter = ClothesColorPresenter(10, (0, 0, 0), (255, 255, 255), (255, 255, 255), 15, 15, 5)
        image_draw = frame.copy()
        for i, region in enumerate(region_s):
            clothes_color_s = ClothesColorDetector.detect_clothes_color(image_draw, region)
            image_draw = presenter.insert(image_draw, clothes_color_s, region)
        cv2.imshow("frame 0", image_draw)
        cv2.waitKey(delay)
