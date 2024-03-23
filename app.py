# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import cv2
import dlib
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import joblib

app = Flask(__name__)

# Load Dlib models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the trained k-NN model if available
try:
    classifier = joblib.load('face_recognition_model.joblib')
    label_encoder = joblib.load('label_encoder.joblib')
except FileNotFoundError:
    classifier = None
    label_encoder = None

# Function to compute the face embedding
def get_face_embedding(face):
    shape = predictor(face, dlib.rectangle(0, 0, face.shape[0], face.shape[1]))
    return shape

# Function to train a face recognition model
def train_face_recognition(embeddings, labels):
    # Convert labels to integers
    global label_encoder
    label_encoder = {label: idx for idx, label in enumerate(set(labels))}
    labels_numeric = [label_encoder[label] for label in labels]

    # Convert embeddings to a numpy array
    embeddings_np = np.array(embeddings)

    # Train the k-NN classifier
    global classifier
    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(embeddings_np, labels_numeric)

    # Save the trained model and label encoder to files
    joblib.dump(classifier, 'face_recognition_model.joblib')
    joblib.dump(label_encoder, 'label_encoder.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get user input
    name = request.form['name']
    age = request.form['age']
    image = request.files['image']

    # Save the image
    image.save('static/uploads/' + image.filename)

    # Read the saved image for face recognition
    img = cv2.imread('static/uploads/' + image.filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Face detection
    faces = detector(gray)

    if len(faces) == 0:
        return jsonify({'error': 'No face detected'})

    # Assume the first detected face is the user's face
    face_bb = faces[0]
    aligned_face = img[face_bb.top():face_bb.bottom(), face_bb.left():face_bb.right()]

    # Compute the face embedding
    face_embedding = get_face_embedding(aligned_face)

    # Assume label is the user's name
    label = name

    if classifier is not None:
        # Train the face recognition model
        train_face_recognition([face_embedding], [label])

    # Add heart rate measurement logic here

    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
