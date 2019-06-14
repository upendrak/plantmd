FROM python:slim-stretch
MAINTAINER Upendra Devisetty <upendrakumar.devisetty@gmail.com>
LABEL Description "This App is meant for Disease prediction from Keras model"

# Update the OS
RUN apt-get update

# Copy the files into the container
COPY . /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Install the dependencies
RUN pip install Werkzeug Flask numpy Keras gevent pillow h5py tensorflow

# Expose the port
EXPOSE 5000

# Run the app
CMD [ "python" , "app.py"]

