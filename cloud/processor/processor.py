import paho.mqtt.client as mqtt
import boto3

s3client = boto3.client('s3')

LOCAL_NQTT_HOST="mosquitto-service"
MQTT_PORT=1883
MQTT_TOPIC="faces"

count = 0
def save_img(img_bytes):
    global count
    response = s3client.put_object( 
    Bucket='alicehua-w251-hw3',
    Body=img_bytes,
    Key='face{:d}.png'.format(count),
    ACL='public-read',
    ContentType='image/png'
  )
    count+=1


def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client,userdata, msg):
    print("Let's save some images...")
    try:
        print("message received! {} bytes".format(len(msg.payload)))    
        # now we need to write the msg to s3
        save_img(msg.payload)
    except Exception:
        print("Unexpected error:", sys.exec_info()[0])


print("Create new instance")
local_mqttclient = mqtt.Client()

print("Bind call back function")
local_mqttclient.on_connect = on_connect_local

print("Connect to broker")
local_mqttclient.connect(LOCAL_MQTT_HOST, MQTT_PORT)

print("Saving images...")
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()

