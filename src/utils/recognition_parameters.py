from dataclasses import dataclass

@dataclass
class RecognitionParameters:
	frame_resize_scale: float
	rec_tolerance: float
	known_face_rect_color: tuple
	unknown_face_rect_color: tuple
	face_rect_text_color: tuple
	face_rect_thick: int
	face_rect_text_scale: float
	face_rect_text_thick: int