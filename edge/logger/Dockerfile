#FROM ubuntu:latest
# this is needed to make sure we can see the log output
#ENV PYTHONUNBUFFERED=1
#WORKDIR /app

#ENV DEBIAN_FRONTEND noninteracive
#RUN apt-get update
#RUN apt install -y python3-dev python3-pip python3-opencv vim-tiny libopencv-dev mosquitto-clients 
#RUN pip3 install paho-mqtt
#COPY listener.py listener.py
#CMD python3 listener.py

FROM ubuntu:latest
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install paho-mqtt 
COPY logger.py ./
CMD ["python3","logger.py"]



