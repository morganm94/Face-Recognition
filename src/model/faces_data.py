import numpy as np
from dataclasses import dataclass

@dataclass
class FacesData:
	src_imgs: list
	encodings: list
	names: list