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

1. Run `auto-py-to-exe`
2. Load JSON configuration
3. Convert

## How to launch Qt5 designer

1. Activate venv
2. Launch designer
```
pyqt5-tools designer
```
