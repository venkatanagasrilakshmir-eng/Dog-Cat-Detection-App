from flask import Flask, render_template, request
import os
import cv2
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model/svm_model.pkl', 'rb'))

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['file']

    if file:

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        image = cv2.imread(filepath)
        image = cv2.resize(image, (64,64))
        image = image.flatten().reshape(1,-1)

        prediction = model.predict(image)

        result = "🐱 Cat" if prediction[0] == 0 else "🐶 Dog"

        return render_template(
            'index.html',
            prediction=result,
            image_path=filepath
        )

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
