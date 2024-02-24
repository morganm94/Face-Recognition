import numpy as np
from dataclasses import dataclass

@dataclass
class FacesData:
	src_imgs: np.ndarray
	encodings: np.ndarray
	names: np.ndarray