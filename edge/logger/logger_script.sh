#!/bin/bash 

if [ "$1"  == run ]; then
   kubectl apply -f logger_deployment.yaml
else 
   kubectl delete deployment logger-deployment
fi



