import cv2
import numpy as np

class Video(object):
    def __init__(self, videoName):
        self.video = cv2.VideoCapture(videoName)

    def __del__(self):
        self.video.release()

    def get_frame(self):

        ret, frame = self.video.read()

        # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        ret, jpg = cv2.imencode('.jpg', frame)

        return jpg.tobytes()