import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.colorchooser import askcolor
import VideoFaceRecognition as VFR

class FaceRecognitionApp:

    def __init__(self, title, geometry):
        self.__root = tk.Tk()
        self.__root.title(title)
        self.__root.geometry(geometry)

        self.__root.columnconfigure(0, weight = 1)
        self.__root.columnconfigure(1, weight = 1)
        
        self.__root.rowconfigure(0, weight = 1)
        self.__root.rowconfigure(1, weight = 1)
        self.__root.rowconfigure(2, weight = 1)
        self.__root.rowconfigure(3, weight = 1)
        self.__root.rowconfigure(4, weight = 1)
        self.__root.rowconfigure(5, weight = 1)
        
        openVideoBtn = ttk.Button(
            text = "Open Video", 
            command = self.__openVideoFile
        )
        openVideoBtn.grid(row = 0, column = 0)

        loadFacesBtn = ttk.Button(
            text = "Load Faces", 
            command = self.__openFaceImages
        )
        loadFacesBtn.grid(row = 1, column = 0)
        
        recAndShowBtn = ttk.Button(
            text = "Execute", 
            command = self.__recognizeAndShow
        )
        recAndShowBtn.grid(row = 2, column = 0)
        
        rectColorChooserBtn = ttk.Button(
            text = "Set Face Rect Color", 
            command = self.__setFaceRectColor
        )
        rectColorChooserBtn.grid(row = 4, column = 0)
        
        faceNameColorBtn = ttk.Button(
            text = "Set Face Name Color", 
            command = self.__setFaceNameColor
        )
        faceNameColorBtn.grid(row = 5, column = 0)

        self.__root.mainloop()

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
            self.__videoFilePath = pathToVideo
    
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
            self.__facesFilePath = pathToFaces
    
    def __setFaceRectColor(self):
        color = askcolor(title="Select face rectangle color")
    
        if color is not None:
            self.__faceRectColor = color[0]
    
    def __setFaceNameColor(self):
        color = askcolor(title="Select face name color")
    
        if color is not None:
            self.__faceNameColor = color[0]
    
    def __recognizeAndShow(self):
        vfr = VFR.VideoFaceRecognition(
            self.__videoFilePath, 
            self.__facesFilePath
        )
        
        try:
            vfr.faceRectColor = self.__faceRectColor
        except:
            pass
        
        try:
            vfr.faceNameColor = self.__faceNameColor
        except:
            pass
    
        vfr.recognizeAndShow()


