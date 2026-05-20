import os
import cv2
import numpy as np
import pickle

from sklearn.svm import SVC

data = []
labels = []

categories = ['cats', 'dogs']

for category in categories:

    path = os.path.join('dataset/train', category)
    label = categories.index(category)

    for img in os.listdir(path):

        try:
            img_path = os.path.join(path, img)

            image = cv2.imread(img_path)
            image = cv2.resize(image, (64,64))

            data.append(image.flatten())
            labels.append(label)

        except:
            pass

X = np.array(data)
y = np.array(labels)

model = SVC(kernel='linear')
model.fit(X, y)

pickle.dump(model, open('model/svm_model.pkl', 'wb'))

print("Model Trained Successfully")
