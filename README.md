# W251 - Summmer 2021 - Homework 3
### Section 2: Alice Hua

This repository contains my homework 3 **Containers, Kubernetes, and IoT/Edge** for W251 - Deep Learning in the Cloud and at the Edge at the UC Berkeley School of Information. 
The following is the directory structure of this application.

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
![](images/hw3.png)

MQTT is a lightweight messaging protocol for Internet of Things (IoT). The MQTT system contains brokers and clients, 
where clients can be either publishers or subscribers or both. Publishers 
- MQTT Topic & Quality of Service (QoS): 

`insert image here`

### Assumptions & Requirements

### Example Images
- My S3 Bucket: https://alicehua-w251-hw3.s3.amazonaws.com/
- My sample image:https://alicehua-w251-hw3.s3.amazonaws.com/face10684.png
![](images/face0.png)
 
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

