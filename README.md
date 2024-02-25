# Face Recognition App

## Installation and launch

1. Install Python 3.8
2. Upgrade pip
3. Clone this repository
4. Activate venv
```python
python -m venv .venv
```
```python
.venv\Scripts\activate
```
For deactivate
```python
deactivate
```
5. Install submodules
```
git submodule update --init
```
6. Install face recognition library
```python
python -m pip install libs\face_recog_dlib_file\dlib-19.19.0-cp38-cp38-win_amd64.whl
```
7. Install packages
```python
python -m pip install -r requirements.txt
```
> ⚠️ Warning! `face-recognition-models` has a large size
8. Launch
```python
python src/app.py
```

## Build with PyInstaller

1. Open
```
.venv\Lib\site-packages\face_recognition\api.py
```
2. Replace
```
pose_predictor_68_point = dlib.shape_predictor(predictor_68_point_model)
```
```
pose_predictor_5_point = dlib.shape_predictor(predictor_5_point_model)
```
```
cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_face_detection_model)
```
```
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)
```
to
```
pose_predictor_68_point = r"%cd%\.venv\Lib\site-packages\face_recognition_models\models\shape_predictor_68_face_landmarks.dat"
```
```
pose_predictor_5_point = r"%cd%\.venv\Lib\site-packages\face_recognition_models\models\shape_predictor_5_face_landmarks.dat"
```
```
cnn_face_detector = r"%cd%\.venv\Lib\site-packages\face_recognition_models\models\mmod_human_face_detector.dat"
```
```
face_encoder = r"%cd%\.venv\Lib\site-packages\face_recognition_models\models\dlib_face_recognition_resnet_model_v1.dat"
```
3. Run `build.bat`

## How to launch Qt5 designer

1. Activate venv
2. Launch designer
```
pyqt5-tools designer
```
