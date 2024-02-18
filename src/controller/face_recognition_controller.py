from PyQt5.QtGui import QPixmap, QColor
from model.face_recognition_model import FaceRecognitionModel as FRM
from utils.cv_to_qt_converter import *

class FaceRecognitionController:
	
	def __init__(self, view, model):
		self.__view = view

		self.__model = model
		self.__model.change_image_signal.connect(self.__update_image)

		self.__view.controller = self
		self.__view.change_image_output_size_signal.connect(self.__set_output_image_size)

		self.__output_img_width = 1280
		self.__output_img_height = 720

		self.start_recognition()

		self.__view.show()

	def set_stream_src(self, stream) -> None:
		self.__model.stream_src = stream

	def stop_recognition(self) -> None:
		self.__model.stop()

	def start_recognition(self) -> None:
		self.__model.start()

	def __set_output_image_size(self, size) -> None:
		self.__output_img_width = size[0]
		self.__output_img_height = size[1]

	def __update_image(self, cv_img) -> None:
		img = convert_cv_to_qt(
			cv_img, 
			self.__output_img_width, 
			self.__output_img_height
		)
		self.__view.update_image(img)
