# Face Recognition App

## Installation and launch

1. Install Python 3.8
2. Upgrade pip
3. Clone this repository
4. Activate venv
5. Install submodules
```
git submodule update --init
```
6. Install face recognition library
```python
pip install libs\face_recog_dlib_file\dlib-19.19.0-cp38-cp38-win_amd64.whl
```
7. Install packages
```python
pip install -r requirements.txt
```
> ⚠️ Warning! `face-recognition-models` has a large size
8. Launch
```python
python src/app.py
```

## How to launch Qt5 designer

1. Activate venv
2. Launch designer
```
pyqt5-tools designer
```
