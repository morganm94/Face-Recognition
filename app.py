from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.colorchooser import askcolor
import VideoFaceRecognition as VFR

root = Tk()
root.title("Face Recognition")
root.geometry("300x200")

def openVideoFile():
    global videoFilePath

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
        videoFilePath = pathToVideo

def openFaceImages():
    global facesFilePath

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
        facesFilePath = pathToFaces

def setFaceRectColor():
    global faceRectColor

    color = askcolor(title="Select face rectangle color")

    if color is not None:
        faceRectColor = color[0]

def setFaceNameColor():
    global faceNameColor

    color = askcolor(title="Select face name color")

    if color is not None:
        faceNameColor = color[0]

def recognizeAndShow():
    vfr = VFR.VideoFaceRecognition(videoFilePath, facesFilePath)
    
    try:
        vfr.faceRectColor = faceRectColor
    except:
        pass
    
    try:
        vfr.faceNameColor = faceNameColor
    except:
        pass

    vfr.recognizeAndShow()

openVideoBtn = ttk.Button(
    text="Open Video", 
    command=openVideoFile
).pack(fill=X)

loadFacesBtn = ttk.Button(
    text="Load Faces", 
    command=openFaceImages
).pack(fill=X)

recAndShowBtn = ttk.Button(
    text="Execute", 
    command=recognizeAndShow
).pack(fill=X)

horizontalSeparator = ttk.Separator(
    master=root,
    orient=HORIZONTAL
).pack(fill=X, pady=10,)

rectColorChooserBtn = ttk.Button(
    text="Set Face Rect Color", 
    command=setFaceRectColor
).pack(fill=X)

faceNameColorBtn = ttk.Button(
    text="Set Face Name Color", 
    command=setFaceNameColor
).pack(fill=X)

root.mainloop()
