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

        self.__prepareFaceImages()
        self.__videoTitle = Path(self.__pathToVideo).stem

    def recognizeAndShow(self):
        video = cv2.VideoCapture(self.__pathToVideo)
    
        while True:
            ret, frame = video.read()

            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            if self.__processThisFrame:
                smallFrame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
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
                        tolerance=0.8
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

                top *= 2
                right *= 2
                bottom *= 2
                left *= 2

                cv2.rectangle(
                    frame, 
                    (left, top), 
                    (right, bottom), 
                    (0, 0, 255), 
                    2
                )
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(
                    frame, 
                    name,
                    (left, bottom + 30), 
                    font, 
                    1.0, 
                    (255, 255, 255), 
                    2
                )

            resizedFrame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            cv2.imshow(self.__videoTitle, resizedFrame)

            key = cv2.waitKey(1)

            if key == 27:
                break

        video.release()
        cv2.destroyAllWindows()

    def __prepareFaceImages(self):
        for path in self.__pathToFaces:
            img = frn.load_image_file(path)
            self.__faceImages.append(img)

            fe = frn.face_encodings(img)[0]
            self.__knownFaceEncodings.append(fe)

            fileName = Path(path).stem
            self.__knownFaceNames.append(fileName)
