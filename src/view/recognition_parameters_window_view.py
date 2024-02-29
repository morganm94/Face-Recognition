from copy import deepcopy
from PyQt5.QtWidgets import QDialog, QColorDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from .recognition_parameters_window import Ui_Form as rpw_ui_form
from utils.recognition_parameters import RecognitionParameters

class RecognitionParametersWindowView(QDialog):

	changed_recognition_params_signal = pyqtSignal(RecognitionParameters)

	def __init__(self, params) -> None:
		super(QDialog, self).__init__(None)

		self.__params = params

		self.__ui = rpw_ui_form()
		self.__ui.setupUi(self)

		self.__set_combobox_values()
		self.__set_connections()
		self.__set_parameters()

	def __set_combobox_values(self) -> None:
		scales = ["0.25", "0.5", "1.0"]

		self.__ui.scale_x_comboBox.addItems(scales)
		self.__ui.scale_x_comboBox.setCurrentText("0.5")

	def __set_parameters(self) -> None:
		self.__ui.scale_x_comboBox.setCurrentText(
			str(self.__params.frame_resize_scale)
		)
		self.__ui.recog_error_doubleSpinBox.setValue(
			self.__params.rec_tolerance
		)
		self.__ui.scale_signature_doubleSpinBox.setValue(
			self.__params.face_rect_text_scale
		)
		self.__ui.thickness_frame_spinBox.setValue(
			self.__params.face_rect_thick
		)
		self.__ui.thickness_signature_spinBox.setValue(
			self.__params.face_rect_text_thick
		)
		self.__selected_rect_color = self.__params.known_face_rect_color
		self.__unselected_rect_color = self.__params.unknown_face_rect_color
		self.__face_rect_text_color = self.__params.face_rect_text_color

	def __return_parameters(self) -> None:
		new_params = deepcopy(self.__params)
		
		new_params.frame_resize_scale = float(
			self.__ui.scale_x_comboBox.currentText()
		)
		new_params.rec_tolerance = self.__ui.recog_error_doubleSpinBox.value()
		new_params.known_face_rect_color = self.__selected_rect_color
		new_params.unknown_face_rect_color = self.__unselected_rect_color
		new_params.face_rect_text_color = self.__face_rect_text_color
		new_params.face_rect_thick = self.__ui.thickness_frame_spinBox.value()
		new_params.face_rect_text_scale = self.__ui.scale_signature_doubleSpinBox.value()
		new_params.face_rect_text_thick = self.__ui.thickness_signature_spinBox.value()

		self.changed_recognition_params_signal.emit(new_params)

	def __choose_color(self, current) -> tuple:
		current_color = QColor(current[2], current[1], current[0])
		selected_color = QColorDialog.getColor(current_color)

		if selected_color.isValid():
			return (
				selected_color.blue(), 
				selected_color.green(), 
				selected_color.red()
			)
		else:
			return current

	def __set_selected_rect_color(self) -> None:
		self.__selected_rect_color = self.__choose_color(
			self.__selected_rect_color
		)

	def __set_unselected_rect_color(self) -> None:
		self.__unselected_rect_color = self.__choose_color(
			self.__unselected_rect_color
		)

	def __set_face_rec_text_color(self) -> None:
		self.__face_rect_text_color = self.__choose_color(
			self.__face_rect_text_color
		)

	def __set_connections(self) -> None:
		self.__ui.ok_pushButton.clicked.connect(
			self.__return_parameters
		)
		self.__ui.color_selected_recog_toolButton.clicked.connect(
			self.__set_selected_rect_color
		)
		self.__ui.color_unselected_recog_toolButton.clicked.connect(
			self.__set_unselected_rect_color
		)
		self.__ui.color_signature_recog_toolButton.clicked.connect(
			self.__set_face_rec_text_color
		)