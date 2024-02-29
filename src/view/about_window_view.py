from .about_window_ui import Ui_AboutProgrammDialog
from PyQt5.QtWidgets import QDialog

class AboutWindowView(QDialog):

	def __init__(self):
		super(QDialog, self).__init__(None)

		self.__ui = Ui_AboutProgrammDialog()
		self.__ui.setupUi(self)