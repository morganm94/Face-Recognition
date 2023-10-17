import face_recognition as frn
import numpy as np
import cv2

class VideoFaceRecognition:

    def __init__(self, videoPath, facesPath):
        self.videoPath = videoPath
        self.facesPath = facesPath
