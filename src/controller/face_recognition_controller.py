from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QMessageBox
from view.recognition_parameters_window_view import RecognitionParametersWindowView
from model.face_recognition_model import FaceRecognitionModel as FRM
from model.recognition_preparing import *
from utils.cv_to_qt_converter import *
from utils.stream_types import StreamTypes
from utils.recognition_parameters import RecognitionParameters

class FaceRecognitionController:
	
	def __init__(self, main_view, main_model):
		self.__main_view = main_view
		self.__model = main_model

		self.__main_view.controller = self
		self.__connect_signals()

		self.__output_img_width = 1280
		self.__output_img_height = 720

		self.__main_view.show()

	def set_stream_src(self, stream) -> None:
		self.__model.stream_src = stream

	def __stop_recognition(self) -> None:
		self.__model.stop()

	def __start_recognition(self) -> None:
		self.__model.start()

	def __open_parametres_win(self) -> None:
		self.__parameters_win = RecognitionParametersWindowView(
			self.__model.recognition_params
		)
		self.__parameters_win.show()

		self.__parameters_win.changed_recognition_params_signal.connect(
			self.__recognition_parameters_changed
		)

	def __set_output_image_size(self, size) -> None:
		self.__output_img_width = size[0]
		self.__output_img_height = size[1]

	def __update_image(self, cv_img) -> None:
		img = convert_cv_to_qt(
			cv_img, 
			self.__output_img_width, 
			self.__output_img_height
		)
		self.__main_view.update_image(img)

	def __load_face_images(self, paths_to_imgs) -> None:
		self.__model.faces_data = prepare_faces_data(paths_to_imgs)

	def __set_video_str_path(self, path) -> None:
		self.__model.video_src = path

	def __set_stream_type(self, stream_type) -> None:
		self.__model.stream_src = stream_type

	def __recognition_parameters_changed(self, params: RecognitionParameters) -> None:
		self.__model.recognition_params = params

	def __show_empy_path_error(self) -> None:
		usr_responce = QMessageBox.warning(
			self.__main_view, 
			"Внимание!",
			"Видео для распознавания не загружено",
			QMessageBox.Cancel
		)

		self.__main_view.reset_recognition_status()

	def __connect_signals(self) -> None:
		self.__model.change_image_signal.connect(self.__update_image)
		self.__model.on_empty_video_path_signal.connect(self.__show_empy_path_error)
		self.__main_view.change_image_output_size_signal.connect(
			self.__set_output_image_size
		)
		self.__main_view.open_recognition_parameters_win_signal.connect(
			self.__open_parametres_win
		)
		self.__main_view.start_recognition_signal.connect(
			self.__start_recognition
		)
		self.__main_view.stop_recognition_signal.connect(
			self.__stop_recognition
		)
		self.__main_view.face_images_load_signal.connect(
			self.__load_face_images
		)
		self.__main_view.video_src_load_signal.connect(
			self.__set_video_str_path
		)
		self.__main_view.stream_src_type_signal.connect(
			self.__set_stream_type
		)