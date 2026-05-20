# 🐶🐱 Dog vs Cat Detection Web App using SVM

A professional Machine Learning web application that classifies images of cats and dogs using a Support Vector Machine (SVM) model.  
Built with Flask, OpenCV, Scikit-learn, HTML, CSS, and JavaScript.

---

# 🚀 Project Overview

This project uses Machine Learning techniques to detect whether an uploaded image contains a **Cat 🐱** or a **Dog 🐶**.

The application provides:

- Image Upload Feature
- Real-Time Prediction
- Professional Responsive UI
- SVM Classification Model
- Flask Backend Integration

---

# 🌟 Features

✅ Upload Cat/Dog Images  
✅ Predict Animal using SVM  
✅ Modern Professional UI  
✅ Responsive Web Design  
✅ Image Preview  
✅ Fast Prediction  
✅ Flask Backend  
✅ Machine Learning Integration  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Flask | Web Framework |
| OpenCV | Image Processing |
| Scikit-learn | Machine Learning |
| NumPy | Data Handling |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| JavaScript | Frontend Interaction |

---

# 📁 Project Structure

```plaintext
Dog-Cat-Detection-App/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── model/
│   └── svm_model.pkl
│
├── dataset/
│   ├── train/
│   │   ├── cats/
│   │   └── dogs/
│   │
│   └── test/
│       ├── cats/
│       └── dogs/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   ├── uploads/
│   │
│   └── images/
│       ├── bg.jpg
│       ├── cat.png
│       └── dog.png
│
├── templates/
│   └── index.html
│
└── utils/
    └── preprocess.py
```

---

# 🧠 Machine Learning Workflow

## Step 1 — Dataset Collection

- Download Kaggle Cats vs Dogs dataset
- Organize images into folders

---

## Step 2 — Image Preprocessing

- Resize images
- Convert images into feature vectors
- Normalize data

---

## Step 3 — Model Training

The project uses the Support Vector Machine (SVM) algorithm for image classification.

### SVM Formula

\[
f(x) = w^Tx + b
\]

---

## Step 4 — Prediction

- Upload image from frontend
- Backend processes image
- SVM model predicts result
- Output displayed on webpage

---

# 📸 Application Screenshots

## 🏠 Home Page

- Upload image interface
- Prediction button
- Responsive design

## 🔍 Prediction Result

- Uploaded image preview
- Prediction label
- Professional result card

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Dog-Cat-Detection-App.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Dog-Cat-Detection-App
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Train Model

```bash
python train_model.py
```

---

## 5️⃣ Run Flask Application

```bash
python app.py
```

---

# 🌐 Open in Browser

```plaintext
http://127.0.0.1:5000
```

---

# 📦 requirements.txt

```txt
flask
numpy
opencv-python
scikit-learn
pickle-mixin
```

---

# 🎨 Frontend Highlights

- Glassmorphism UI
- Animated Buttons
- Responsive Layout
- Modern Gradient Background
- Interactive Upload Section

---

# 📈 Future Enhancements

✅ Deep Learning CNN Model  
✅ Real-Time Camera Detection  
✅ Mobile App Version  
✅ User Authentication  
✅ Prediction History  
✅ Accuracy Graphs  
✅ Dark/Light Theme  

---

# 📚 Learning Outcomes

Through this project, you will learn:

- Machine Learning Basics
- SVM Classification
- Flask Web Development
- Image Processing using OpenCV
- Frontend & Backend Integration
- Model Deployment

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Your Name**  
Machine Learning & Web Development Enthusiast

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
