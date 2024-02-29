from face_recognition import load_image_file, face_encodings
from pathlib import Path
from utils.faces_data import FacesData

def prepare_faces_data(paths: list) -> None:
    if not paths:
        return 

    face_images = []
    face_enc = []
    face_names = []

    for path in paths:
        try:
            img = load_image_file(path)
            face_images.append(img)

            fe = face_encodings(img)
            face_enc.append(fe[0])

            file_name = Path(path).stem
            face_names.append(file_name)
        except:
            pass

    return FacesData(face_images, face_enc, face_names)