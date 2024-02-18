import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

def convert_cv_to_qt(cv_img, out_width, out_height) -> QPixmap:
	rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
	
	height, width, channels = rgb_img.shape
	bytes_per_line = channels * width

	qt_img = QImage(
		rgb_img.data, 
		width, 
		height, 
		bytes_per_line, 
		QImage.Format_RGB888
	)
	qt_img_scaled = qt_img.scaled(out_width, out_height, Qt.KeepAspectRatio)

	return QPixmap.fromImage(qt_img_scaled)