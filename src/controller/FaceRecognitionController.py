from model.FaceRecognitionModel import FaceRecognitionModel as FRM

class FaceRecognitionController:
	
	def __init__(self, view, model):
		self.__view = view
		self.__model = model

		self.__view.controller = self
		#self.__view.show()