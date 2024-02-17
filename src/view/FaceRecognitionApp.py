import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
import model.VideoFaceRecognition as VFR

class FaceRecognitionApp:
    
    __videoFileTypes = [
        ("Video", ".mp4 .avi"),
        ("MP4", ".mp4"),
        ("AVI", ".avi")
    ]

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

        self.__videoFileOperations = [
            "Recognize And Show", 
            "Recognize Aad Save"
        ]
        self.__videoFileOperationsDefaultValue = tk.StringVar(
            value = self.__videoFileOperations[0]
        )

    def __createWidgets(self):
        openVideoBtn = ttk.Button(
            text = "Open Video", 
            command = self.__openVideoFile
        )
        openVideoBtn.grid(row = 0, column = 0, sticky = "nswe")
        
        loadFacesBtn = ttk.Button(
            text = "Load Faces", 
            command = self.__openFaceImages
        )
        loadFacesBtn.grid(row = 1, column = 0, sticky = "nswe")

        self.__saveVideoBtn = ttk.Button(
            text = "Save Video",
            command = self.__saveVideoFile,
            state = tk.DISABLED
        )
        self.__saveVideoBtn.grid(row = 2, column = 0, sticky = "nswe")
                
        self.__recAndShowBtn = ttk.Button(
            text = "Execute", 
            command = self.__recognizeAndShow,
            state = tk.DISABLED
        )
        self.__recAndShowBtn.grid(row = 3, column = 0, sticky = "nswe")
                
        rectColorChooserBtn = ttk.Button(
            text = "Set Face Rect Color", 
            command = self.__setFaceRectColor
        )
        rectColorChooserBtn.grid(row = 4, column = 0, sticky = "nswe")
                
        faceNameColorBtn = ttk.Button(
            text = "Set Face Name Color: ", 
            command = self.__setFaceNameColor
        )
        faceNameColorBtn.grid(row = 5, column = 0, sticky = "nswe")

        smallFrameScaleLabel = ttk.Label(
            text = "Small Frame Size: ",
            anchor = tk.CENTER
        )
        smallFrameScaleLabel.grid(row = 0, column = 1, sticky = "e")

        smallFrameScaleSB = ttk.Spinbox(
            from_ = 0.1,
            to = 1.0,
            increment = 0.1,
            command = self.__setSmallFrameScale,
            wrap = True,
            textvariable = self.smallFrameScaleDefaultValue,
        )
        smallFrameScaleSB.grid(row = 0, column = 2, sticky = "we")

        faceRecognitionToleranceLabel = ttk.Label(
            text = "Face Recognition Tolerance: ",
            anchor = tk.CENTER
        )
        faceRecognitionToleranceLabel.grid(row = 1, column = 1, sticky = "e")

        faceRecognitionToleranceSB = ttk.Spinbox(
            from_ = 0.1,
            to = 1.0,
            increment = 0.1,
            command = self.__setFaceRecognitionTolerance,
            wrap = True,
            textvariable = self.faceRecognitionToleranceDefaultValue
        )
        faceRecognitionToleranceSB.grid(row = 1, column = 2, sticky = "we")

        outputFrameScaleLabel = ttk.Label(
            text = "Output Frame Scale: ",
            anchor = tk.CENTER
        )
        outputFrameScaleLabel.grid(row = 2, column = 1, sticky = "e")

        outputFrameScaleSB = ttk.Spinbox(
            from_ = 0.1,
            to = 1.0,
            increment = 0.1,
            command = self.__setOutputFrameScale,
            wrap = True,
            textvariable = self.outputFrameScaleDefaultValue
        )
        outputFrameScaleSB.grid(row = 2, column = 2, sticky = "we")

        videoFileOperationsLabel = ttk.Label(
            text = "Actions: ",
            justify = tk.RIGHT,
            anchor = tk.CENTER
        )
        videoFileOperationsLabel.grid(row = 3, column = 1, sticky = "e")

        self.__videoFileOperationsCB = ttk.Combobox(
            values = self.__videoFileOperations,
            textvariable = self.__videoFileOperationsDefaultValue
        )
        self.__videoFileOperationsCB.grid(row = 3, column = 2,  sticky = "we")
        self.__videoFileOperationsCB.bind(
            "<<ComboboxSelected>>", 
            self.__setVideoFileOperation
        )

    def __setVideoFileOperation(self, event):
        selection = self.__videoFileOperationsCB.get()

        if selection ==  self.__videoFileOperations[0]:
            self.__vfr.changeVideoOperationType(True)
            self.__saveVideoBtn.config(state = "disabled")
        elif selection == self.__videoFileOperations[1]:
            self.__vfr.changeVideoOperationType(False)
            self.__saveVideoBtn.config(state = "normal")

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

    def __saveVideoFile(self):
        pathToSave = filedialog.asksaveasfilename(
            title = "Save video as",
            filetypes = self.__videoFileTypes
        )

        if pathToSave != "":
            self.__vfr.pathToSaveVideo = pathToSave
        
    def __openVideoFile(self):
        pathToVideo = filedialog.askopenfilename(
            title = "Select video file",
            filetypes = self.__videoFileTypes,
            multiple = False
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

