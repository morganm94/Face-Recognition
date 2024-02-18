import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread

class FaceRecognitionModel(QThread):

    change_image_signal = pyqtSignal(np.ndarray)
    
    def __init__(self):
        super().__init__()

        self.__is_recognition_enabled = False

    def run(self) -> None:
        webcam_capture = cv2.VideoCapture(0)
        self.__is_recognition_enabled = True
        
        while self.__is_recognition_enabled:
            ret, frame = webcam_capture.read()

            if ret:
                self.change_image_signal.emit(frame)

        webcam_capture.release()

    def stop(self) -> None:
        self.__is_recognition_enabled = False
        self.wait()