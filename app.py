import os
import cv2
import tensorflow as tf
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Initialize Flask App
app = Flask(__name__)

# Set Upload Folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load Trained Model
model = load_model("/Users/harshravani/shivam/Hibicuious Project/hibiscus_cnn_model.h5")

# Define Class Labels
categories = ["Hibiscus_rosa-sinensis", "Hibiscus_sabdariffa", "Hibiscus_mutabilis"]

# Function to Predict Image
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))  
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0) 

    prediction = model.predict(img_array)
    predicted_label = categories[np.argmax(prediction)]
    return predicted_label

# Route for Main Page
@app.route('/')
def index():
    return render_template('index.html')

# Route for Handling File Upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    predicted_class = predict_image(file_path)
    return jsonify({'prediction': predicted_class, 'image_url': url_for('uploaded_file', filename=file.filename)})

# Route to Serve Uploaded Files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route to Capture Image Using OpenCV
@app.route('/capture')
def capture_image():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Capture Image - Press "C" to Capture', frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], "captured.jpg")
            cv2.imwrite(img_path, frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    
    predicted_class = predict_image(img_path)
    return jsonify({'prediction': predicted_class, 'image_url': url_for('uploaded_file', filename="captured.jpg")})

if __name__ == '__main__':
    app.run(debug=True)
