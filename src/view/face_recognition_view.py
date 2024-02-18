import numpy as np
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from .test_ui import Ui_MainWindow
from controller.face_recognition_controller import FaceRecognitionController

class FaceRecognitionView(QMainWindow):

	change_image_output_size_signal = pyqtSignal(tuple)
	
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

	@pyqtSlot(np.ndarray)
	def update_image(self, image) -> None:
		self.__ui.imageOutput.setPixmap(image)

	def closeEvent(self, event) -> None:
		self.__controller.stop_recognition()
		event.accept()

	def resizeEvent(self, event) -> None:
		imageOutputNewSize = (
			self.__ui.imageOutput.width(), 
			self.__ui.imageOutput.height()
		)
		self.change_image_output_size_signal.emit(imageOutputNewSize)