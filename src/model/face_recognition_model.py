import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal, QThread
from .recognizer import Recognizer
from utils.faces_data import FacesData
from utils.stream_types import StreamTypes
from utils.recognition_parameters import RecognitionParameters

class FaceRecognitionModel(QThread):

    change_image_signal = pyqtSignal(np.ndarray)
    
    def __init__(self):
        super().__init__()

        self.__stream_src = StreamTypes.webcam
        self.__video_src_path = None
        self.__is_recognition_enabled = False
        self.__faces_data = None
        self.__rec_params = None

    @property
    def faces_data(self) -> FacesData:
        return self.__faces_data

    @faces_data.setter
    def faces_data(self, value: FacesData) -> None:
        self.__faces_data = value

    @property
    def recognition_params(self) -> RecognitionParameters:
        return self.__rec_params

    @recognition_params.setter
    def recognition_params(self, value: RecognitionParameters) -> None:
        self.__rec_params = value

    @property
    def stream_src(self) -> StreamTypes:
        return self.__stream_src

    @stream_src.setter
    def stream_src(self, value) -> None:
        self.__stream_src = value

    @property
    def video_src(self) -> str:
        return self.__video_src_path

    @video_src.setter
    def video_src(self, value) -> None:
        self.__video_src_path = value

    def run(self) -> None:
        stream_capture = self.__determine_stream_type()

        self.__is_recognition_enabled = True
        process_current_frame = True
        
        while self.__is_recognition_enabled:
            ret, frame = stream_capture.read()

            if process_current_frame and self.__faces_data is not None:
                rgb_frame = self.__bgr_to_rgb_frame(frame)
                scaled_frame = self.__scale_frame(
                    rgb_frame, 
                    self.__rec_params.frame_resize_scale
                )
                recognizer = Recognizer(
                    "Неизвестный",
                    self.__faces_data,
                    self.__rec_params
                )
                faces_locations, faces_names = recognizer.process_current_frame(
                    scaled_frame
                )

            process_current_frame = not process_current_frame

            if self.__faces_data is not None:
                frame = recognizer.identify_faces(
                    frame, faces_locations, faces_names
                )

            self.change_image_signal.emit(frame)

        stream_capture.release()

    def stop(self) -> None:
        self.__is_recognition_enabled = False
        self.wait()

    def __determine_stream_type(self) -> cv2.VideoCapture:
        if self.__stream_src == StreamTypes.video:
            return cv2.VideoCapture(self.__video_src_path)
            
        return cv2.VideoCapture(0)

    def __bgr_to_rgb_frame(self, frame: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def __scale_frame(self, frame: np.ndarray, scale: float) -> np.ndarray:
        return cv2.resize(frame, (0, 0), fx=scale, fy=scale)