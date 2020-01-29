from __future__ import division, print_function
# coding=utf-8
import streamlit as st
from PIL import Image
import os
import numpy as np
import json
import predict
from keras.models import load_model

# Model path
folder_path = "./models"
model_name = "model_vgg16_2.hdf5"
model_file = os.path.join(folder_path, model_name)

# Load your trained model
model = load_model(model_file)

st.markdown("<h1 style='text-align: left; color: green;'>Welcome to PlantMD!</h1>", unsafe_allow_html=True)
st.write("")

st.sidebar.title('Predict New Images')

img_file_buffer = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if img_file_buffer is not None:
	image = np.array(Image.open(img_file_buffer))
	st.image(image, caption='Uploaded Image.')
	processed_image = predict.preprocess_image(img_file_buffer)
	prediction = predict.model_predict(processed_image, model)
	st.write("### Predictions:")
	res = '%s : %s' % (prediction[0][0], prediction[0][1])
	st.write(res)
	st.write("### Description:")
	descr = predict.description(prediction)
	st.write(descr[0][1])
else:
	# st.sidebar.success("Select an image above.")
	
	st.markdown(
		"""
		PlantMD is a web app that can rapidly and accurately diagnose plant diseases

		👈 Upload an image on the left to see how PlantMD can diagnose diseases for you!

		### Want to learn more about PlantMD?

		- Checkout [github](https://github.com/upendrak/Disease_Predictor) repo
		- Checkout [blog]

		"""
		)
