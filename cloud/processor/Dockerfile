FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
ENV TZ=America
#ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get install -y python3 python3-pip mosquitto-clients
RUN pip3 install paho-mqtt
RUN pip3 install numpy
RUN pip3 install boto3
WORKDIR /app
# example from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_vide$
COPY processor.py ./
CMD ["python3","processor.py"]
