import numpy as np
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from .main_window_ui import Ui_MainWindow
from utils.stream_types import StreamTypes
from controller.face_recognition_controller import FaceRecognitionController

class MainWindowView(QMainWindow):

	change_image_output_size_signal = pyqtSignal(tuple)
	open_recognition_parameters_win_signal = pyqtSignal()
	start_recognition_signal = pyqtSignal()
	stop_recognition_signal = pyqtSignal()
	stream_src_type_signal = pyqtSignal(StreamTypes)
	face_images_load_signal = pyqtSignal(np.ndarray)
	video_src_load_signal = pyqtSignal(str)

	is_can_start_recognition = True
	
	def __init__(self):
		super(QMainWindow, self).__init__(None)

		self.__ui = Ui_MainWindow()
		self.__ui.setupUi(self)
		self.showMaximized()

		self.__controller = None
		self.__set_connections()

	@property
	def controller(self) -> FaceRecognitionController:
		return self.__controller

	@controller.setter
	def controller(self, value) -> None:
		self.__controller = value

	@pyqtSlot(np.ndarray)
	def update_image(self, image) -> None:
		self.__ui.Web_label_2.setPixmap(image)

	def closeEvent(self, event) -> None:
		self.stop_recognition_signal.emit()
		event.accept()

	def resizeEvent(self, event) -> None:
		imageOutputNewSize = (
			self.__ui.Web_label_2.width(), 
			self.__ui.Web_label_2.height()
		)
		self.change_image_output_size_signal.emit(imageOutputNewSize)

	def __check_video(self) -> None:
		if self.__ui.video_radioButton.isChecked():
			self.stream_src_type_signal.emit(StreamTypes.video)
			self.__ui.loadvideo_pushButton.setEnabled(True)
			self.__ui.webcam_groupBox.setTitle("Видео")

	def __check_web(self) -> None:
		if self.__ui.webcam_radioButton.isChecked():
			self.stream_src_type_signal.emit(StreamTypes.webcam)
			self.__ui.loadvideo_pushButton.setEnabled(False)
			self.__ui.webcam_groupBox.setTitle("Веб-камера")

	def __open_parametres_win(self) -> None:
		self.open_recognition_parameters_win_signal.emit()

	def __loadimages_pushButton_clicked(self) -> None:
		options = QFileDialog.Options()
		selfilter = "Images (*.png *.xpm *.jpg *.jpeg)"
		fileNames, _ = QFileDialog.getOpenFileNames(
			QMainWindow(),
			"Загрузка изображений", 
			"",
			selfilter, 
			options=options
		)

		if fileNames:
			self.face_images_load_signal.emit(np.asarray(fileNames))

	def __loadvideo_pushButton_clicked(self) -> None:
		options = QFileDialog.Options()
		selfilter = "Videos (*.mp4 *.avi *.mpeg)"
		fileName, _ = QFileDialog.getOpenFileName(
			QMainWindow(),
			"Загрузка видео", 
			"",
			selfilter, 
			options=options
		)

		if fileName:
			self.video_src_load_signal.emit(fileName)

	def __recognition_processing(self) -> None:
		if self.is_can_start_recognition:
			self.start_recognition_signal.emit()
			self.__ui.recognise_pushButton.setText("Прекратить")
			self.is_can_start_recognition = False
		else:
			self.stop_recognition_signal.emit()
			self.__ui.recognise_pushButton.setText("Распознать")
			self.is_can_start_recognition = True

	def __set_connections(self) -> None:
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
		self.__ui.recognise_pushButton.clicked.connect(
			self.__recognition_processing
		)