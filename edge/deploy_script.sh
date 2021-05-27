#!/bin/bash 

if [ "$1"  == run ]; then
   kubectl apply -f mosquittoService.yaml 
   kubectl apply -f mosquitto_deployment.yaml
else 
   kubectl delete deployment mosquitto-deployment
   kubectl delete service mosquitto-service
fi




