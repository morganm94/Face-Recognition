from cv2 import COLOR_BGR2RGB, VideoCapture, cvtColor, resize
from numpy import ndarray
from PyQt5.QtCore import pyqtSignal, QThread
from .recognizer import Recognizer
from utils.faces_data import FacesData
from utils.stream_types import StreamTypes
from utils.recognition_parameters import RecognitionParameters

class FaceRecognitionModel(QThread):

    change_image_signal = pyqtSignal(ndarray)
    on_empty_video_path_signal = pyqtSignal()
    
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

        if stream_capture is None:
            return

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

    def __determine_stream_type(self) -> VideoCapture:
        if self.__stream_src == StreamTypes.video:
            if self.__video_src_path is not None:
                return VideoCapture(self.__video_src_path)
            else:
                self.on_empty_video_path_signal.emit()
                return None
        else:
            return VideoCapture(0)

    def __bgr_to_rgb_frame(self, frame: ndarray) -> ndarray:
        return cvtColor(frame, COLOR_BGR2RGB)

    def __scale_frame(self, frame: ndarray, scale: float) -> ndarray:
        return resize(frame, (0, 0), fx=scale, fy=scale)