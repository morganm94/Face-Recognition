import numpy as np
import face_recognition as frn
from pathlib import Path
from utils.faces_data import FacesData

def prepare_faces_data(paths: np.ndarray) -> None:
    if not paths.size:
        return None

    imgs_count = paths.size

    face_images = np.zeros(imgs_count, dtype=np.ndarray)
    face_enc = np.zeros(imgs_count, dtype=np.ndarray)
    face_names = np.zeros(imgs_count, dtype=np.ndarray)

    for i in range(imgs_count):
        img = frn.load_image_file(paths[i])
        face_images[i] = img

        fe = frn.face_encodings(img)[0]
        face_enc[i] = fe

        file_name = Path(paths[i]).stem
        face_names[i] = file_name
        
    return FacesData(face_images, face_enc, face_names)