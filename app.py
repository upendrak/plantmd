from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import operator
import json

# Keras
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, jsonify
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = "models/AlexNetModel.hdf5"

# Load your trained model
model = load_model(MODEL_PATH)
model._make_predict_function()  # Necessary
print('Model loaded. Check http://127.0.0.1:5000/')

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x/255

    predictions = model.predict(x)
    pred_5 = np.argsort(predictions)[0][-3:]
    top_5 = {}
    labels_dict = {'Apple Scab': 0, 'Apple Black rot': 1, 'Apple Cedar rust': 2, 'Apple healthy': 3, 'Blueberry healthy': 4, 'Cherry(Sour) Mildew': 5, 'Cherry(Sour) healthy': 6, 'Corn Leaf spot': 7, 'Corn Common rust': 8, 'Corn Northern Leaf Blight': 9, 'Corn healthy': 10, 'Grape Black rot': 11, 'Grape Black measles': 12, 'Grape Leaf Blight': 13, 'Grape healthy': 14, 'Citrus greening': 15, 'Peach Bacterial spot': 16, 'Peach healthy': 17, 'Bell_Pepper Bacterial spot': 18, 'Bell_Pepper healthy': 19, 'Potato Early Blight': 20, 'Potato Late Blight': 21, 'Potato healthy': 22, 'Raspberry healthy': 23, 'Soybean healthy': 24, 'Squash Powdery mildew': 25, 'Strawberry Leaf scorch': 26, 'Strawberry healthy': 27, 'Tomato Bacterial spot': 28, 'Tomato Early blight': 29, 'Tomato Late blight': 30, 'Tomato Leaf Mold': 31, 'Tomato Septoria leaf spot': 32, 'Tomato Two-spotted spider mite': 33, 'Tomato Target Spot': 34, 'Tomato Yellow Leaf Curl Virus': 35, 'Tomato mosaic virus': 36, 'Tomato healthy': 37}
    for i in pred_5:
        rank = predictions[0][i]
        for kee, val in labels_dict.items():
            if i == val:
                top_5[kee] = round(rank * 100, 3)

    sorted_x2 = sorted(top_5.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_x2

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        result = model_predict(file_path, model)

        result2 = dict(result)
        top_hit = list(result2.keys())[0]
        top_val = list(result2.values())[0]
        dis_file = "models/disease_description.csv"
        result_final = {}
        with open(dis_file, 'r') as fh_in:
            for line in fh_in:
                line = line.strip().split(",")
                result_final[line[0]] = line[1]
        result = {}
        for kee, val in result_final.items():
            if top_hit in kee:
                new = top_hit + " - "+ str(top_val)
                result[new] = val
        
        # Prediction + Description
        return jsonify({'payload':json.dumps([{'name':kee, 'val':val} for kee, val in result.items()])})

    return None

if __name__ == '__main__':

    # Serve the app with gevent
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
