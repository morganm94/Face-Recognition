# Face Recognition and Heart Rate Measurement Project

## Description
This project combines Smart Face Recognition and Heart Rate Measurement to provide a simple yet impactful solution. Users can register by entering their name, age, and uploading a picture. The system then uses face recognition to identify the user and measures their heart rate through the camera. The project showcases the power of innovation in a compact package, offering enhanced security and wellness monitoring.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/devbluecomet/Face-Recognition.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Face-Recognition
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the Dlib shape predictor model:
   - Download [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
   - Extract the file and place it in the project directory.

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open a web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the application.

3. Register by entering your name, age, and uploading a picture.

4. Click on "Check Heart Rate" to initiate face recognition and heart rate measurement.

## Acknowledgments
- This project utilizes the Dlib library for face detection and shape prediction.
- The heart rate measurement is a simulated demo and requires integration with a suitable heart rate measurement library.

