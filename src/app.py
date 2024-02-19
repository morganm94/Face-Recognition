import sys
from PyQt5.QtWidgets import QApplication
from view.main_window_view import MainWindowView as MWV
from model.face_recognition_model import FaceRecognitionModel as FRM
from controller.face_recognition_controller import FaceRecognitionController as FRC

def main():
    app = QApplication(sys.argv)
    model = FRM()
    view = MWV()
    controller = FRC(view, model)
    app.exec()

if __name__ == "__main__":
    sys.exit(main())