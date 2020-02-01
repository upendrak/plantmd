# Deploy PlantMD with Streamlit as Web App 

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3.svg)]()
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Docker Pulls](https://img.shields.io/docker/pulls/upendradevisetty/diseasepredictor.svg)](https://hub.docker.com/r/upendradevisetty/diseasepredictor/)
[![Docker Stars](https://img.shields.io/docker/stars/evolinc/rmta.svg)](https://hub.docker.com/r/upendradevisetty/diseasepredictor/)
[![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/upendradevisetty/diseasepredictor.svg)](https://hub.docker.com/r/upendradevisetty/diseasepredictor/)

## Getting started

- Clone this repo 
- Install requirements (Or use Docker)
- Run the script with Streamlit after installing the dependencies (Or run the Docker container)
- Upload a test image
- Check http://localhost:8501/
- Done! :tada:

:point_down:Screenshots:

<p align="center">
  <img src="https://i.postimg.cc/K8yJxgj7/plantmd-ss-1.png" width="600px" alt="">
</p>

<p align="center">
  <img src="https://i.postimg.cc/P5RJ11DY/plantmd-ss-2.png" width="600px" alt="">
</p>

------------------

## Docker Installation

> Docker can be installed on any of three platform using the instructions from [Docker](https://docs.docker.com/engine/installation/) website. You can also try [Play-With-Docker](http://labs.play-with-docker.com/) without installing Docker on your computer 

### Pull and run a built-image from Docker hub without building the image 
```shell
$ git clone https://github.com/upendrak/Disease_Predictor.git && cd Disease_Predictor
$ docker run --rm -p 8501:8501 upendradevisetty/diseasepredictor:1.0 
```
Open http://localhost:8501/ on your computer to load the dashboard

## Non-Docker Installation (Not recommended)

### Clone the repo
```shell
$ git clone https://github.com/upendrak/Disease_Predictor.git && cd Disease_Predictor
```

### Install requirements after creating a virtual environment
```shell
$ python3 -m vevn plantmd_venv
$ source plantmd_venv/bin/activate
$ pip3 install -r requirements.txt
```

### Run with Streamlit
```shell
$ streamlit run demo.py
```
