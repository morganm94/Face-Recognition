from pathlib import Path
import face_recognition as frn
import numpy as np
import cv2

class VideoFaceRecognition:

    def __init__(self, pathToVideo, pathToFaces):
        self.__pathToVideo = pathToVideo
        self.__pathToFaces = pathToFaces

        self.__faceImages = []
        self.__knownFaceEncodings = []
        self.__knownFaceNames = []

        self.__processThisFrame = True
        self.__repeatVideo = False
        self.__smallFrameScale = 0.5
        self.__faceRecognitionTolerance = 0.8
        self.__outputFrameScale = 1.0
        self.__faceRectColor = (255, 0, 0)
        self.__faceNameColor = (255, 255, 255)

        self.__prepareFaceImages()
        self.__videoTitle = Path(self.__pathToVideo).stem

    @property
    def repeatVideo(self) -> float:
        return self.__repeatVideo

    @repeatVideo.setter
    def repeatVideo(self, value) -> None:
        if (type(value) is not bool):
            raise ValueError("The value must be 'True' or 'False'")

        self__repeatVideo = value

    @property
    def smallFrameScale(self) -> float:
        return self.__smallFrameScale

    @smallFrameScale.setter
    def smallFrameScale(self, value: float) -> None:
        if (value <= 0.0 or value > 1.0):
            raise ValueError("The value must be in range (0.0, 1.0]")

        self.__smallFrameScale = value

    @property
    def faceRecognitionTolerance(self) -> float:
        return self.__faceRecognitionTolerance

    @faceRecognitionTolerance.setter
    def faceRecognitionTolerance(self, value: float) -> None:
        if (value <= 0.0 or value > 1.0):
            raise ValueError("The value must be in range (0.0, 1.0]")

        self.__faceRecognitionTolerance = value

    @property
    def outputFrameScale(self) -> float:
        return self.__outputFrameScale

    @outputFrameScale.setter
    def outputFrameScale(self, value: float) -> None:
        if (value <= 0.0 or value > 1.0):
            raise ValueError("The value must be in range (0.0, 1.0]")

        self.__outputFrameScale = value

    @property
    def faceRectColor(self) -> tuple:
        return self.__faceRectColor

    @faceRectColor.setter
    def faceRectColor(self, color: tuple) -> None:
        if (not color or len(color) < 3):
            raise ValueError("The value must be, for example, (134, 255, 11)")

        self.__faceRectColor = self.__convertBGR2RGB(color)

    @property
    def faceNameColor(self) -> tuple:
        return self.__faceNameColor

    @faceNameColor.setter
    def faceNameColor(self, color: tuple) -> None:
        if (not color or len(color) < 3):
            raise ValueError("The value must be, for example, (134, 255, 11)")

        self.__faceNameColor = self.__convertBGR2RGB(color)

    def recognizeAndShow(self) -> None:
        video = cv2.VideoCapture(self.__pathToVideo)
    
        while True:
            ret, frame = video.read()

            if not ret and self.__repeatVideo:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            if self.__processThisFrame:
                smallFrame = cv2.resize(
                    frame, 
                    (0, 0), 
                    fx=self.__smallFrameScale, 
                    fy=self.__smallFrameScale
                )
                rgbSmallFrame = cv2.cvtColor(smallFrame, cv2.COLOR_BGR2RGB)

                faceLocations = frn.face_locations(rgbSmallFrame)
                faceEncodings = frn.face_encodings(
                    rgbSmallFrame, 
                    faceLocations
                )

                faceNames = []

                for fe in faceEncodings:
                    matches = frn.compare_faces(
                        self.__knownFaceEncodings,
                        fe,
                        tolerance=self.__faceRecognitionTolerance
                    )

                    name = None
                    
                    faceDistances = frn.face_distance(
                        self.__knownFaceEncodings, 
                        fe
                    )
                    bestMatchIndex = np.argmin(faceDistances)

                    if matches[bestMatchIndex]:
                        name = self.__knownFaceNames[bestMatchIndex]

                    faceNames.append(name)

            self.__processThisFrame = not self.__processThisFrame

            for (
                top, right, bottom, left
            ), name in zip(faceLocations, faceNames):
                if not name:
                    continue

                top, right, bottom, left = self.__scaleFaceLocation(
                    top, right, bottom, left
                )

                cv2.rectangle(
                    frame, 
                    (left, top), 
                    (right, bottom), 
                    self.__faceRectColor, 
                    2
                )
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(
                    frame, 
                    name,
                    (left, bottom + 30), 
                    font, 
                    1.0, 
                    self.__faceNameColor,
                    2
                )

            resizedFrame = cv2.resize(
                frame, 
                (0, 0), 
                fx=self.__outputFrameScale, 
                fy=self.__outputFrameScale
            )
            cv2.imshow(self.__videoTitle, resizedFrame)

            key = cv2.waitKey(1)

            if key == 27:
                break

        video.release()
        cv2.destroyAllWindows()

    def __prepareFaceImages(self) -> None:
        if not self.__pathToFaces:
            return 

        for path in self.__pathToFaces:
            img = frn.load_image_file(path)
            self.__faceImages.append(img)

            fe = frn.face_encodings(img)[0]
            self.__knownFaceEncodings.append(fe)

            fileName = Path(path).stem
            self.__knownFaceNames.append(fileName)

    def __scaleFaceLocation(self, top, right, bottom, left) -> list:
        scaleMultiplier = int(1 / self.__smallFrameScale)

        top    *= scaleMultiplier 
        right  *= scaleMultiplier 
        bottom *= scaleMultiplier 
        left   *= scaleMultiplier 

        return top, right, bottom, left

    def __convertBGR2RGB(self, color: tuple) -> tuple:
        return (color[2], color[1], color[0])
