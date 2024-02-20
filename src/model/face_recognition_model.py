import cv2
import numpy as np
import face_recognition as frn
from pathlib import Path
from PyQt5.QtCore import pyqtSignal, QThread
from utils.faces_data import FacesData
from utils.stream_types import StreamTypes
from utils.recognition_parameters import RecognitionParameters

class FaceRecognitionModel(QThread):

    change_image_signal = pyqtSignal(np.ndarray)

    __UNKNOWN_FACE_TITLE = "Неизвестный"
    
    def __init__(self):
        super().__init__()

        self.__stream_src = StreamTypes.webcam
        self.__face_images = None
        self.__video_src_path = None
        self.__is_recognition_enabled = False
        self.__faces_data = None

        self.__rec_params = RecognitionParameters(
            0.5, 0.5, 0.6, (0, 255, 0), (0, 0, 255), (255, 0, 0), 1, 1.0, 1
        )

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

            if process_current_frame:
                scaled_frame = cv2.resize(
                    frame, 
                    (0, 0), 
                    fx=self.__rec_params.fx_resize_scale, 
                    fy=self.__rec_params.fy_resize_scale
                )
                rgb_scaled_frame = cv2.cvtColor(
                    scaled_frame, cv2.COLOR_BGR2RGB
                )

                faces_locations = frn.face_locations(rgb_scaled_frame)
                faces_encodings = frn.face_encodings(
                    rgb_scaled_frame, faces_locations
                )

                faces_names = []

                if self.__faces_data is not None:
                    for fe in faces_encodings:
                        matches = frn.compare_faces(
                            self.__faces_data.encodings,
                            fe,
                            tolerance=self.__rec_params.rec_tolerance
                        )

                        name = self.__UNKNOWN_FACE_TITLE

                        face_distances = frn.face_distance(
                            self.__faces_data.encodings, fe
                        )
                        best_match_index = np.argmin(face_distances)

                        if matches[best_match_index]:
                            name = self.__faces_data.names[best_match_index]

                        faces_names.append(name)

            process_current_frame = not process_current_frame
            
            for (
                top, right, bottom, left
            ), name in zip(faces_locations, faces_names):
                top *= 2
                right *= 2
                bottom *= 2
                left *= 2

                if name == self.__UNKNOWN_FACE_TITLE:
                    rect_color = self.__rec_params.unknown_face_rect_color
                else:
                    rect_color = self.__rec_params.known_face_rect_color

                cv2.rectangle(
                    frame, 
                    (left, top), 
                    (right, bottom), 
                    rect_color, 
                    self.__rec_params.face_rect_thick
                )

                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(
                    frame, 
                    name, 
                    (left, bottom + 30),
                    font, 
                    self.__rec_params.face_rect_text_scale,
                    self.__rec_params.face_rect_text_color,
                    self.__rec_params.face_rect_text_thick
                )

            self.change_image_signal.emit(frame)

        stream_capture.release()

    def stop(self) -> None:
        self.__is_recognition_enabled = False
        self.wait()

    def prepare_face_images(self, path: tuple) -> None:
        if not path:
            return

        face_images = []
        face_enc = []
        face_names = []

        for p in path:
            img = frn.load_image_file(p)
            face_images.append(img)

            fe = frn.face_encodings(img)[0]
            face_enc.append(fe)

            file_name = Path(p).stem
            face_names.append(file_name)
            
        self.__faces_data = FacesData(face_images, face_enc, face_names)

    def __determine_stream_type(self) -> cv2.VideoCapture:
        if self.__stream_src == StreamTypes.video:
            return cv2.VideoCapture(self.__video_src_path)
            
        return cv2.VideoCapture(0)