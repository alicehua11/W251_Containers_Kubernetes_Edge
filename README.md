# W251 - Summmer 2021 - Homework 3
### Section 2: Alice Hua

This repository contains my homework 3 **Containers, Kubernetes, and IoT/Edge** for W251 - Deep Learning in the Cloud and at the Edge at the UC Berkeley School of Information. 
The following is the directory structure of this application. There are two main components, the edge and the cloud. The edge device is the Jetson NX, the IoT device is the USB webcam. The cloud component is a VM in AWS.
The application is deployed using Kubernetes (K3s)
```
+-- cloud
|   +-- deploy_script.sh
|   +-- broker
|       +-- Dockerfile
|	+-- docker_script.sh
|       +-- mosquitto_deployment.yaml
|       +-- mosquittoService.yaml  
|   +-- processor
|       +-- Dockerfile
|	+-- docker_script.sh
|	+-- processor_deployment.yaml
|	+-- processor.py
+-- edge
|   +-- deploy_script.sh
|   +-- mosquitto_deployment.yaml
|   +-- other_deployments.yaml
|   +-- mosquittoService.yaml
|   +-- broker
|       +-- Dockerfile
|   +-- detector
|	+-- Dockerfile
|       +-- docker_script.sh
|	+-- haarcascade_frontalface_default.xml
|       +-- cam.py
|   +-- logger 
|       +-- Dockerfile
|       +-- docker_script.sh
|       +-- logger.py
|   +-- forwarder
|      +-- Dockerfile
|      +-- docker_script.sh
|      +-- forwarder.py    
```

### How it works
The application capture faces in a video The skeleton 
![](images/hw3.png)

MQTT is a lightweight messaging protocol for Internet of Things (IoT). The MQTT system contains brokers and clients, 
where clients can be either publishers or subscribers or both. Publishers 
- MQTT Topic & Quality of Service (QoS): 

![](images/mqtt.png)

Three Quality of Service (QoS): match network reliability & application logic
0 - At most once (best effort delivery, no guarantee of deliver)
1 - At least once (guarantees delivery of at least one time to receiver, could deliver multiple times)
2 - Exactly one (highest level, guarantees that each message is received on once, safest and slowest quality of service level)


### Assumptions & Requirements
You need to set up a few things for this application to connect:
1. You have a functioning USB webcam + Jetson NX 
2. You have installed k3s & docker on your Jetson and on your VM
1. You have created IAM role with AmazonS3FullAccess policy

### Example Images- My S3 Bucket: https://alicehua-w251-hw3.s3.amazonaws.com/
- My sample image:https://alicehua-w251-hw3.s3.amazonaws.com/face10684.png  
> ![](images/face0.png)
 
### Take Aways
- Learn how to build Docker images from scratch
- Learn how Kubernetes orchestrate pods (where containers live) via Deployments, communicate with each other through ports via Services
- Learn how to use kubectl-cli to interact + debug pods
- Learn what MQTT is, its subscriber/publisher architecture
- Learn how the edge (Jetson) communicates (i.e inbound security) with cloud (AWS EC2)  

### Reference

- MQTT
	- https://mqtt.org/
	- http://event.moxa.com/newsletter/connection/2019/10/feat_02.html
	- http://www.steves-internet-guide.com/client-connections-python-mqtt/
	- https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php

- Kubernetes
	- https://www.youtube.com/watch?v=X48VuDVv0do
	- https://medium.com/@texasdave2/troubleshoot-kubectl-connection-refused-6f5445a396ed
	- https://blog.getambassador.io/kubernetes-ingress-nodeport-load-balancers-and-ingress-controllers-6e29f1c44f2d
- 
- S3
	- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
	- https://stackoverflow.com/questions/40336918/how-to-write-a-file-or-data-to-an-s3-object-using-boto3

