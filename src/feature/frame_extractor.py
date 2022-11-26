import cv2


def extract_frame(video_path, interval=3):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_s = []
    frame_count = 0

    while video.isOpened():
        is_video_not_finished, frame = video.read()
        frame_count += 1
        if not is_video_not_finished:
            break
        if frame_count % (int(fps * interval)) == 0:
            frame_s.append(frame)
    return frame_s
