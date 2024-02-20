from PyQt5.QtWidgets import QWidget
from .recognition_parameters_window import Ui_Form as rpw_ui_form
from utils.recognition_parameters import RecognitionParameters

class RecognitionParametersWindowView(QWidget):

	def __init__(self, params) -> None:
		super(QWidget, self).__init__(None)

		self.__params = params

		self.__ui = rpw_ui_form()
		self.__ui.setupUi(self)

		self.__set_parameters()

	def __set_parameters(self) -> None:
		self.__ui.recog_error_doubleSpinBox.setValue(
			self.__params.rec_tolerance
		)

	def __return_parameters(self) -> None:
		pass