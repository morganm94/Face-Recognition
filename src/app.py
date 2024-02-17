import sys
from view.FaceRecognitionView import FaceRecognitionView as FRV
from model.FaceRecognitionModel import FaceRecognitionModel as FRM
from controller.FaceRecognitionController import FaceRecognitionController as FRC

def main():
    model = FRM()
    view = FRV()
    controller = FRC(view, model)

if __name__ == "__main__":
    sys.exit(main())