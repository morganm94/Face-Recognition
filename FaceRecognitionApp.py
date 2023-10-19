import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.colorchooser import askcolor
import VideoFaceRecognition as VFR

class FaceRecognitionApp:

    def __init__(self, title, geometry):
        self.vfr = VFR.VideoFaceRecognition()

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

        self.__setWidgetsDefaultValues()
        self.__createWidgets()

        self.__root.mainloop()

    def __setWidgetsDefaultValues(self):
        self.smallFrameScaleDefaultValue = tk.DoubleVar(
            value = self.vfr.smallFrameScale
        )

        self.faceRecognitionToleranceDefaultValue = tk.DoubleVar(
            value = self.vfr.faceRecognitionTolerance
        )

        self.outputFrameScaleDefaultValue = tk.DoubleVar(
            value = self.vfr.outputFrameScale
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
                
        recAndShowBtn = ttk.Button(
            text = "Execute", 
            command = self.__recognizeAndShow
        ).grid(row = 2, column = 0, sticky = "nswe")
                
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
        self.vfr.smallFrameScale = self.smallFrameScaleDefaultValue.get()

    def __setFaceRecognitionTolerance(self):
        self.vfr.faceRecognitionTolerance = \
            self.faceRecognitionToleranceDefaultValue.get()

    def __setOutputFrameScale(self):
        self.vfr.outputFrameScale = self.outputFrameScaleDefaultValue.get()
        
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
            self.vfr.pathToVideo = pathToVideo
    
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
            self.vfr.pathToFaces = pathToFaces

    def __openColorSelectionDialog(self, color: tuple, winTitle: str) -> tuple:
        color = askcolor(color=color, title=winTitle)

        if color is not None:
            return color[0]
    
    def __setFaceRectColor(self):
        self.__faceRectColor = self.__openColorSelectionDialog(
            self.vfr.faceRectColor,
            "Select face rectangle color"
        )
        self.vfr.faceRectColor = self.__faceRectColor
    
    def __setFaceNameColor(self):
        self.__faceNameColor = self.__openColorSelectionDialog(
            self.vfr.faceNameColor,
            "Select face name color"
        )
        self.vfr.faceNameColor = self.__faceNameColor
    
    def __recognizeAndShow(self):
        try:
            self.vfr.faceRectColor = self.__faceRectColor
        except:
            pass
        
        try:
            self.vfr.faceNameColor = self.__faceNameColor
        except:
            pass
    
        self.vfr.recognizeAndShow()


