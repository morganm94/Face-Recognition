import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.colorchooser import askcolor
import VideoFaceRecognition as VFR

class FaceRecognitionApp:

    def __init__(self, title, geometry):
        self.__vfr = VFR.VideoFaceRecognition()

        self.__root = tk.Tk()
        self.__root.title(title)
        self.__root.geometry(geometry)

        self.__root.columnconfigure(0, weight = 1)
        self.__root.columnconfigure(1, weight = 1)
        self.__root.columnconfigure(2, weight = 1)
        
        self.__root.rowconfigure(0, weight = 1)
        self.__root.rowconfigure(1, weight = 1)
        self.__root.rowconfigure(2, weight = 1)
        self.__root.rowconfigure(3, weight = 1)
        self.__root.rowconfigure(4, weight = 1)
        self.__root.rowconfigure(5, weight = 1)

        self.__videoUploaded = False
        self.__facesUploaded = False

        self.__setWidgetsDefaultValues()
        self.__createWidgets()

        self.__root.mainloop()

    def __setWidgetsDefaultValues(self):
        self.smallFrameScaleDefaultValue = tk.DoubleVar(
            value = self.__vfr.smallFrameScale
        )

        self.faceRecognitionToleranceDefaultValue = tk.DoubleVar(
            value = self.__vfr.faceRecognitionTolerance
        )

        self.outputFrameScaleDefaultValue = tk.DoubleVar(
            value = self.__vfr.outputFrameScale
        )

    def __createWidgets(self):
        openVideoBtn = ttk.Button(
            text = "Open Video", 
            command = self.__openVideoFile
        ).grid(row = 0, column = 0, sticky = "nswe")
        
        loadFacesBtn = ttk.Button(
            text = "Load Faces", 
            command = self.__openFaceImages
        ).grid(row = 1, column = 0, sticky = "nswe")
                
        self.__recAndShowBtn = ttk.Button(
            text = "Execute", 
            command = self.__recognizeAndShow,
            state = tk.DISABLED
        )
        self.__recAndShowBtn.grid(row = 2, column = 0, sticky = "nswe")
                
        rectColorChooserBtn = ttk.Button(
            text = "Set Face Rect Color", 
            command = self.__setFaceRectColor
        ).grid(row = 4, column = 0, sticky = "nswe")
                
        faceNameColorBtn = ttk.Button(
            text = "Set Face Name Color", 
            command = self.__setFaceNameColor
        ).grid(row = 5, column = 0, sticky = "nswe")

        smallFrameScaleLabel = ttk.Label(
            text = "Small Frame Size",
            anchor = tk.CENTER
        ).grid(row = 0, column = 1, sticky = "nswe")

        smallFrameScaleSB = ttk.Spinbox(
            from_ = 0.1,
            to = 1.0,
            increment = 0.1,
            command = self.__setSmallFrameScale,
            wrap = True,
            textvariable = self.smallFrameScaleDefaultValue,
        ).grid(row = 0, column = 2, sticky = "we")

        faceRecognitionToleranceLabel = ttk.Label(
            text = "Face Recognition Tolerance",
            anchor = tk.CENTER
        ).grid(row = 1, column = 1, sticky = "nswe")

        faceRecognitionToleranceSB = ttk.Spinbox(
            from_ = 0.1,
            to = 1.0,
            increment = 0.1,
            command = self.__setFaceRecognitionTolerance,
            wrap = True,
            textvariable = self.faceRecognitionToleranceDefaultValue
        ).grid(row = 1, column = 2, sticky = "we")

        outputFrameScaleLabel = ttk.Label(
            text = "Output Frame Scale",
            anchor = tk.CENTER
        ).grid(row = 2, column = 1, sticky = "nswe")

        outputFrameScaleSB = ttk.Spinbox(
            from_ = 0.1,
            to = 1.0,
            increment = 0.1,
            command = self.__setOutputFrameScale,
            wrap = True,
            textvariable = self.outputFrameScaleDefaultValue
        ).grid(row = 2, column = 2, sticky = "we")

    def __setSmallFrameScale(self):
        self.__vfr.smallFrameScale = self.smallFrameScaleDefaultValue.get()

    def __setFaceRecognitionTolerance(self):
        self.__vfr.faceRecognitionTolerance = \
            self.faceRecognitionToleranceDefaultValue.get()

    def __setOutputFrameScale(self):
        self.__vfr.outputFrameScale = self.outputFrameScaleDefaultValue.get()

    def __checkPossibilityOfProcessing(self):
        if self.__videoUploaded and self.__facesUploaded:
            self.__recAndShowBtn.config(state = "normal")
    
    def __clearVideoAndImagePaths(self):
        self.__videoUploaded = False
        self.__facesUploaded = False

        self.__recAndShowBtn.config(state = "disabled")
        
    def __openVideoFile(self):
        pathToVideo = filedialog.askopenfilename(
            title="Select video file",
            filetypes=[
                ("Video", ".mp4 .avi"),
                ("MP4", ".mp4"),
                ("AVI", ".avi")
            ],
            multiple=False
        )
    
        if pathToVideo != "":
            self.__vfr.pathToVideo = pathToVideo
            self.__videoUploaded = True
            self.__checkPossibilityOfProcessing()
    
    def __openFaceImages(self):
        pathToFaces = filedialog.askopenfilenames(
            title="Select face images",
            filetypes=[
                ("Images", ".png .jpg .jpeg .webp"),
                ("PNG", ".png"),
                ("JPG", ".jpg"),
                ("JPEG", ".jpeg"),
                ("WEBP", ".webp")
            ],
            multiple=True
        )
    
        if pathToFaces != "":
            self.__vfr.pathToFaces = pathToFaces
            self.__facesUploaded = True
            self.__checkPossibilityOfProcessing()

    def __openColorSelectionDialog(self, color: tuple, winTitle: str) -> tuple:
        color = askcolor(color=color, title=winTitle)

        if color is not None:
            return color[0]
    
    def __setFaceRectColor(self):
        faceRectColor = self.__openColorSelectionDialog(
            self.__vfr.faceRectColor,
            "Select face rectangle color"
        )

        if faceRectColor is not None:
            self.__vfr.faceRectColor = faceRectColor
    
    def __setFaceNameColor(self):
        faceNameColor = self.__openColorSelectionDialog(
            self.__vfr.faceNameColor,
            "Select face name color"
        )

        if faceNameColor is not None:
            self.__vfr.faceNameColor = faceNameColor
    
    def __recognizeAndShow(self):
        self.__vfr.recognizeAndShow()
        self.__clearVideoAndImagePaths()

