#!/bin/bash 

if [ "$1"  == run ]; then
   kubectl apply -f logger_deployment.yaml
   kubectl apply -f mosquittoService.yaml
else 
   kubectl delete deployment logger-deployment
   kubectl delete service mosquitto-service
fi



