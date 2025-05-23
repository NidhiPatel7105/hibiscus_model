Hibiscus Flower Classification Web App 🌺
This project is a web application built with Flask and TensorFlow/Keras that allows users to upload or capture images of hibiscus flowers and classify them into one of three species using a trained Convolutional Neural Network (CNN) model.

🧠 Model
The model (hibiscus_cnn_model.h5) is trained to classify images into the following categories:

Hibiscus_rosa-sinensis
Hibiscus_sabdariffa
Hibiscus_mutabilis
📁 Project Structure
├── app.py # Flask app for web interface and prediction ├── capture.py # Standalone script for capturing an image via webcam ├── hibiscus_cnn_model.h5 # Pre-trained CNN model ├── templates/ │ └── index.html # HTML template (not included here, needs to be added) ├── static/ │ └── uploads/ # Stores captured/uploaded images ├── uploads/ # Used by Flask to save uploaded images

bash Copy Edit

🚀 How to Run the App
Clone the repository:
git clone https://github.com/your-username/hibiscus-flower-classifier.git
cd hibiscus-flower-classifier
Install dependencies:

bash Copy Edit pip install -r requirements.txt Run the web app:

bash Copy Edit python app.py Open your browser and go to:

cpp Copy Edit http://127.0.0.1:5000/ 📸 Capture from Webcam (optional) You can run capture.py to capture an image using your webcam:

bash Copy Edit python capture.py The captured image will be saved in static/uploads/.

📝 Requirements Create a requirements.txt with the following content:

nginx Copy Edit Flask opencv-python tensorflow numpy 📌 Notes Make sure the hibiscus_cnn_model.h5 is placed in the correct path.

You need to provide your own index.html file under templates/.
