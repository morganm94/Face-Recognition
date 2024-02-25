from numpy import ndarray
from dataclasses import dataclass

@dataclass
class FacesData:
	src_imgs: ndarray
	encodings: ndarray
	names: ndarray