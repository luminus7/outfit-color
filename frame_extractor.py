import cv2


# Get Video file's route
class FrameExtractor:
    def __init__(self, video_path):
        self.__video_path = video_path  # input frame
        
    def extract_frame(self):
        # Get Video file
        video = cv2.VideoCapture(video_path)
        fps = video.get(cv2.CAP_PROP_FPS)
        frame_s = []
        frame_count = 0

        while video.isOpened():
            is_video_not_finished, frame = video.read()
            frame_count += 1
            if not is_video_not_finished:
                break
            if frame_count % (int(fps * 3)) == 0:
                frame_s.append(frame)
            # frame_s.append(frame)
        return frame_s


# Show frame #0 => Test is done successfully
if __name__ == "__main__":
    # video_path = ".\\videos\\people_walking.mp4"
    video_path = ".\\videos\\EarthCam - Dublin.mp4"
    video_frame_s = FrameExtractor.extract_frame(video_path)
    print(len(video_frame_s))
    cv2.imshow("frame 0", video_frame_s[0])
    cv2.waitKey()
