from numpy import ndarray, zeros
from face_recognition import load_image_file, face_encodings
from pathlib import Path
from utils.faces_data import FacesData

def prepare_faces_data(paths: ndarray) -> None:
    if not paths.size:
        return None

    imgs_count = paths.size

    face_images = zeros(imgs_count, dtype=ndarray)
    face_enc = zeros(imgs_count, dtype=ndarray)
    face_names = zeros(imgs_count, dtype=ndarray)

    for i in range(imgs_count):
        img = load_image_file(paths[i])
        face_images[i] = img

        fe = face_encodings(img)[0]
        face_enc[i] = fe

        file_name = Path(paths[i]).stem
        face_names[i] = file_name
        
    return FacesData(face_images, face_enc, face_names)