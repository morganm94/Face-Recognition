import sys
from PyQt5.QtWidgets import QApplication
from view.main_window_view import MainWindowView as MWV
from model.face_recognition_model import FaceRecognitionModel as FRM
from controller.face_recognition_controller import FaceRecognitionController as FRC
from utils.recognition_parameters import RecognitionParameters

if getattr(sys, 'frozen', False):
    import pyi_splash

__DEFAULT_RECOGNITION_PARAMETERS = RecognitionParameters(
    0.5,
    0.6, 
    (0, 255, 0), 
    (0, 0, 255), 
    (255, 0, 0), 
    1, 
    1.0, 
    1
)

def main():
    app = QApplication(sys.argv)

    model = FRM()
    model.recognition_params = __DEFAULT_RECOGNITION_PARAMETERS

    view = MWV()
    
    controller = FRC(view, model)

    if getattr(sys, 'frozen', False):
        pyi_splash.close()

    app.exec()

if __name__ == "__main__":
    sys.exit(main())