import numpy as np
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from .main_window_ui import Ui_MainWindow
from controller.face_recognition_controller import FaceRecognitionController

class MainWindowView(QMainWindow):

	change_image_output_size_signal = pyqtSignal(tuple)
	open_recognition_parameters_win_signal = pyqtSignal()
	
	def __init__(self):
		super(QMainWindow, self).__init__(None)

		self.__ui = Ui_MainWindow()
		self.__ui.setupUi(self)

		self.__controller = None
		self.__set_connections()

	@property
	def controller(self):
		return self.__controller

	@controller.setter
	def controller(self, value) -> None:
		self.__controller = value

	@pyqtSlot(np.ndarray)
	def update_image(self, image) -> None:
		self.__ui.Web_label_2.setPixmap(image)

	def closeEvent(self, event) -> None:
		self.__controller.stop_recognition()
		event.accept()

	def resizeEvent(self, event) -> None:
		imageOutputNewSize = (
			self.__ui.Web_label_2.width(), 
			self.__ui.Web_label_2.height()
		)
		self.change_image_output_size_signal.emit(imageOutputNewSize)

	def __check_video(self):
		if self.__ui.video_radioButton.isChecked():
			self.__ui.loadvideo_pushButton.setEnabled(True)

	def __check_web(self):
		if self.__ui.webcam_radioButton.isChecked():
			self.__ui.loadvideo_pushButton.setEnabled(False)

	def __open_parametres_win(self):
		self.open_recognition_parameters_win_signal.emit()

	def __loadimages_pushButton_clicked(self):
		options = QFileDialog.Options()
		selfilter = "Images (*.png *.xpm *.jpg *.jpeg)"
		fileName = QFileDialog.getOpenFileNames(
			QMainWindow(),
			"Загрузка изображений", 
			"",
			selfilter, 
			options=options
		)

	def __loadvideo_pushButton_clicked(self):
		options = QFileDialog.Options()
		selfilter = "Videos (*.mp4 *.avi *.mpeg)"
		fileName = QFileDialog.getOpenFileName(
			QMainWindow(),
			"Загрузка видео", 
			"",
			selfilter, 
			options=options
		)

	def __set_connections(self):
		self.__ui.video_radioButton.clicked.connect(self.__check_video)
		self.__ui.webcam_radioButton.clicked.connect(self.__check_web)
		self.__ui.parametres_pushButton.clicked.connect(
			self.__open_parametres_win
		)
		self.__ui.loadimages_pushButton.clicked.connect(
        	self.__loadimages_pushButton_clicked
        )
		self.__ui.loadvideo_pushButton.clicked.connect(
			self.__loadvideo_pushButton_clicked
		)