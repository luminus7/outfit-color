import cv2


# Get Video file's route
def extract_frame(video_path):
    # Get Video file
    video = cv2.VideoCapture(video_path)
    # fps = video.get(cv2.CAP_PROP_FPS)
    frame_s = []
    frame_count = 0

    while video.isOpened():
        is_video_not_finished, frame = video.read()
        frame_count += 1
        if not is_video_not_finished:
            break
        frame_s.append(frame)
    return frame_s


# Show frame #0 => Test is done successfully
if __name__ == "__main__":
    video_path = ".\\videos\\people_walking.mp4"
    video_frame_s = extract_frame(video_path)
    print(len(video_frame_s))
    cv2.imshow("frame 0", video_frame_s[0])
    cv2.waitKey()