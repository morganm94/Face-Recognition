from PyQt5.QtGui import QPixmap, QColor
from model.face_recognition_model import FaceRecognitionModel as FRM
from utils.cv_to_qt_converter import *

class FaceRecognitionController:
	
	def __init__(self, view, model):
		self.__view = view
		self.__model = model

		self.__view.controller = self
		self.__view.show()

		self.frm = FRM()
		self.frm.change_image_signal.connect(self.__update_image)
		self.frm.start()

	def stop_recognition(self) -> None:
		self.frm.stop()

	def __update_image(self, cv_img) -> None:
		width = 800
		height = 800

		img = convert_cv_to_qt(cv_img, width, height)
		self.__view.set_image(img)
