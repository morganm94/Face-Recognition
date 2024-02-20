from PyQt5.QtWidgets import QWidget, QColorDialog
from .recognition_parameters_window import Ui_Form as rpw_ui_form
from utils.recognition_parameters import RecognitionParameters

class RecognitionParametersWindowView(QWidget):

	def __init__(self, params) -> None:
		super(QWidget, self).__init__(None)

		self.__params = params

		self.__ui = rpw_ui_form()
		self.__ui.setupUi(self)

		self.__set_connections()
		self.__set_parameters()

	def __set_parameters(self) -> None:
		self.__ui.recog_error_doubleSpinBox.setValue(
			self.__params.rec_tolerance
		)

	def __return_parameters(self) -> None:
		pass

	def __choose_color(self) -> tuple:
		color = QColorDialog.getColor()

		return color

	def __set_selected_rect_color(self) -> None:
		print(self.__choose_color())

	def __set_connections(self) -> None:
		self.__ui.color_selected_recog_toolButton.clicked.connect(
			self.__set_selected_rect_color
		)