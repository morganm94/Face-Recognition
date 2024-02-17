from controller.FaceRecognitionController import FaceRecognitionController

class FaceRecognitionView:
	
	def __init__(self):
		self.__controller = None

	@property
	def controller(self):
		return self.__controller

	@controller.setter
	def controller(self, value) -> None:
		self.__controller = value