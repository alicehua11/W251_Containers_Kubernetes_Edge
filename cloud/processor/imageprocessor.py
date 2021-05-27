import numpy as np
import cv2
import paho.mqtt.client as mqtt
import boto3

LOCAL_NQTT_HOST=""
MQTT_PORT=1883
MQTT_TOPIC="faces"


s3client = boto3.client()

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(MQTT_TOPIC)
