import numpy as np
import cv2
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        
local_mqttclient = mqtt.Client()
local_mqttclient.loop_start()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
print('Connected to local broker')

cam = cv2.VideoCapture("/dev/video0")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cam.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        face = gray[y:y+h, x:x+w]
        rc,png = cv2.imencode('.png', face)
        msg = png.tobytes()
        #print(msg)
        try:
            local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg, qos=0, retain=False)
        except Exception as e:
            print(e)
       # frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
       # cv2.imshow('feed', frame)
    # quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
