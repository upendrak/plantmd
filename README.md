# Deploy PlantMD with Streamlit as Web App 

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3.svg)]()
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Docker Pulls](https://img.shields.io/docker/pulls/upendradevisetty/diseasepredictor.svg)](https://hub.docker.com/r/upendradevisetty/plantmd/)
[![Docker Stars](https://img.shields.io/docker/stars/evolinc/rmta.svg)](https://hub.docker.com/r/upendradevisetty/plantmd/)
<a href="https://de.cyverse.org/de/?type=quick-launch&quick-launch-id=8e002616-e030-4ee1-bcaf-e6ce20986e14&app-id=c148e480-4fff-11ea-b1a6-008cfa5ae621" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a>

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

## Run on CyVerse Discovery Environment

> Alternatively you can run the Plantmd on CyVerse Discovery Environment. However you need to register to CyVerse before you can use. More information about user registration can be found [here](https://user.cyverse.org/)

> After you register, you click the below button to launch Plantmd on CyVerse [Discovery Environment](https://de.cyverse.org/)

<a href="https://de.cyverse.org/de/?type=quick-launch&quick-launch-id=8e002616-e030-4ee1-bcaf-e6ce20986e14&app-id=c148e480-4fff-11ea-b1a6-008cfa5ae621" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a>

