from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from .test_ui import Ui_MainWindow
from controller.face_recognition_controller import FaceRecognitionController

class FaceRecognitionView(QMainWindow):
	
	def __init__(self):
		super(QMainWindow, self).__init__(None)
		self.__controller = None
		self.__ui = Ui_MainWindow()
		self.__ui.setupUi(self)

	@property
	def controller(self):
		return self.__controller

	@controller.setter
	def controller(self, value) -> None:
		self.__controller = value

	def set_image(self, image):
		self.__ui.imageOutput.setPixmap(image)

	def closeEvent(self, event):
		self.__controller.stop_recognition()
		event.accept()