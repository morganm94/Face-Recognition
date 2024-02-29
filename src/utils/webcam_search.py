from cv2 import VideoCapture

def get_webcam_list() -> list:
	availabel_webcams_ids = list()
	number_or_iterations = 5

	for i in range(number_or_iterations):
		cap = VideoCapture(i)

		if cap.read()[0]:
			availabel_webcams_ids.append(i)
			cap.release()

	return availabel_webcams_ids