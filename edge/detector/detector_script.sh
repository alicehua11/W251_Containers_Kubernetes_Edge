#!/bin/bash 

if [ "$1"  == run ]; then
   kubectl apply -f detector_deployment.yaml
   #sudo xhost +
   #export DISPLAY=:0
else 
   kubectl delete deployment detector-deployment
fi



