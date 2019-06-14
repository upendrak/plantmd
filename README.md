# Deploy Disease Predict Keras Model with Flask as Web App 

[![](https://img.shields.io/badge/python-2.7%2C%203.5%2B-green.svg)]()
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

## Getting started in 10 minutes

- Clone this repo 
- Install requirements
- Run the script
- Check http://localhost:5000
- Done! :tada:

:point_down:Screenshot:

<p align="center">
  <img src="https://i.postimg.cc/4xjy7cN8/disease-predict-demo.png" width="600px" alt="">
</p>

------------------

## Docker Installation

### Build and run an image for keras-application pretrained model 
```shell
$ git clone https://github.com/upendrak/Disease_Predictor.git
$ cd Disease_Predictor
$ docker build -t keras_flask_app .
$ docker run --rm -d -p 5000:5000 keras_flask_app 
```

### Pull and run a built-image from Docker hub without building the image
```shell
$ git clone https://github.com/upendrak/Disease_Predictor
$ cd Disease_Predictor
$ docker run -d -p 5000:5000 diseasepredict_flask_app
```
Open http://0.0.0.0:5000/ after waiting for a minute to install in the container.

## Non-Docker Installation (not recommended)

### Clone the repo
```shell
$ git clone https://github.com/upendrak/Disease_Predictor.git
$ cd Disease_Predictor
```

### Install requirements

```shell
$ pip install -r requirements.txt
```

Make sure you have the following installed:
- tensorflow
- keras
- flask
- pillow
- h5py
- gevent

### Run with Python

Python 2.7 or 3.5+ are supported and tested (Python 2.7 is not recommended)

```shell
$ python app.py
```