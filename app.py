from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import VideoFaceRecognition as VFR

root = Tk()
root.title("Face Recognition")
root.geometry("300x200")

def openVideoFile():
    global videoFilePath

    pathToVideo = filedialog.askopenfilename()

    if pathToVideo != "":
        videoFilePath = pathToVideo

def openFaceImages():
    global facesFilePath

    pathToFaces = filedialog.askopenfilenames()

    if pathToFaces != "":
        facesFilePath = pathToFaces

def recognizeAndShow():
    vfr = VFR.VideoFaceRecognition(videoFilePath, facesFilePath)
    vfr.recognizeAndShow()

openVideoBtn = ttk.Button(text="Open Video", command=openVideoFile)
openVideoBtn.pack(fill=X)

loadFacesBtn = ttk.Button(text="Load Faces", command=openFaceImages)
loadFacesBtn.pack(fill=X)

recAndShowBtn = ttk.Button(text="Execute", command=recognizeAndShow)
recAndShowBtn.pack(fill=X)

root.mainloop()
