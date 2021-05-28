#!/bin/bash 

if [ "$1"  == run ]; then 
   kubectl apply -f ~/broker/mosquitto_deployment.yaml
   kubectl apply -f ~/broker/mosquittoService.yaml
   kubectl apply -f ~/processor/processor_deployment.yaml
   kubectl expose deployment mosquitto-deployment --type=NodePort --port=32364 --name=mosqu$
else
   kubectl delete deployment mosquitto-deployment
   kubectl delete deployment processor-deployment 
   kubectl delete service mosquitto-service
   kubectl delete service mosquitto
fi

