# from threading import Thread
# import cv2
# from data_structure import thread_safe_queue as tsq
#
# class FrameExtractorMulti:
#     """
#     Class that continuously gets frames from a VideoCapture object
#     with a dedicated thread.
#     """
#
#     def __init__(self, queue, src):
#         self.__src = src
#         self.stream = cv2.VideoCapture(self.__src) # init OpenCV VideoCapture object, src might be first frame
#         (self.grabbed, self.frame) = self.stream.read()
#         self.stopped = False    # flag to show the thread should stop grabbing new frames.
#         self.__queue = queue
#
#     def start(self):
#         Thread(target=self.get, args=()).start()
#         return self
#
#     # This function continuously runs a while loop
#     #  that reads a frame from the video stream and
#     #  stores it in the class instance’s frame attribute,
#     #  as long as the stopped flag isn’t set.
#     def get(self):
#         while not self.stopped:
#             if not self.grabbed:
#                 self.stop()
#             else:
#                 (self.grabbed, self.frame) = self.stream.read()
#
#     # flag setter to indicate stop sign
#     def stop(self):
#         self.stopped = True
#
#     def run(self):
#         # Dedicated thread for grabbing video frames
#         #  with FrameExtractorMulti object.
#         # Main thread shows video frames.
#
#         frame_getter = FrameExtractorMulti(self.__queue, self.__src).start()
#
#         while True:
#             if (cv2.waitKey(1) == ord("q")) or frame_getter.stopped:
#                 frame_getter.stop()
#                 break
#
#             self.__queue.push(frame_getter.frame)
#             # cv2.imshow("Video", self.__queue.pop())
#             # cv2.waitKey()
#
# # Show frame #0 => Test is done successfully
# if __name__ == "__main__":
#     video_path = ".\\videos\\people_walking.mp4"
#     # video_path = ".\\videos\\EarthCam - Dublin.mp4"
#     queue = tsq.ThreadSafeQueue()
#     video_frame_s = FrameExtractorMulti(queue, video_path).run()
#     while queue.size()!=0:
#         cv2.imshow("Video", queue.pop())
#         cv2.waitKey()
