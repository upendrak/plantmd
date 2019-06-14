# Deploy Disease Predict Keras Model with Flask as Web App 

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3.svg)]()
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Docker Pulls](https://img.shields.io/docker/pulls/upendradevisetty/diseasepredictor.svg)](https://hub.docker.com/r/upendradevisetty/diseasepredictor/)
[![Docker Stars](https://img.shields.io/docker/stars/evolinc/rmta.svg)](https://hub.docker.com/r/upendradevisetty/diseasepredictor/)
[![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/upendradevisetty/diseasepredictor.svg)](https://hub.docker.com/r/upendradevisetty/diseasepredictor/)

## Getting started

- Clone this repo 
- Install requirements (Or use Docker)
- Run the script (Or run the Docker container)
- Check http://0.0.0.0:5000/
- Done! :tada:

:point_down:Screenshot:

<p align="center">
  <img src="https://i.postimg.cc/4xjy7cN8/disease-predict-demo.png" width="600px" alt="">
</p>

------------------

## Docker Installation

> Docker can be installed on any of three platform using the instructions from [Docker](https://docs.docker.com/engine/installation/) website. You can also try [Play-With-Docker](http://labs.play-with-docker.com/) without installing Docker on your computer 

### Build and run an image for keras-application pretrained model 
```shell
$ git clone https://github.com/upendrak/Disease_Predictor.git && cd Disease_Predictor
$ wget -O models/AlexNetModel.hdf5 https://de.cyverse.org/dl/d/555373A4-7A0E-48C2-A09B-B1DE8BE7915A/AlexNetModel.hdf5
$ docker build -t keras_flask_app .
$ docker run -v $PWD:/data -w /data --rm -p 5000:5000 keras_flask_app 
```

### Pull and run a built-image from Docker hub without building the image
```shell
$ git clone https://github.com/upendrak/Disease_Predictor.git && cd Disease_Predictor
$ wget -O models/AlexNetModel.hdf5 https://de.cyverse.org/dl/d/555373A4-7A0E-48C2-A09B-B1DE8BE7915A/AlexNetModel.hdf5
$ docker run -v $PWD:/data -w /data --rm -p 5000:5000 upendradevisetty/diseasepredictor:1.0
```
Open http://0.0.0.0:5000/ after waiting for few seconds for the model to load.

## Non-Docker Installation (Not recommended)

### Clone the repo
```shell
$ git clone https://github.com/upendrak/Disease_Predictor.git && cd Disease_Predictor
$ wget -O models/AlexNetModel.hdf5 https://de.cyverse.org/dl/d/555373A4-7A0E-48C2-A09B-B1DE8BE7915A/AlexNetModel.hdf5
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

```shell
$ python app.py
```
