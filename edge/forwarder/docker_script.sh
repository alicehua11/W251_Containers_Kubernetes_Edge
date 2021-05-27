docker build -t forwarder --no-cache .
docker tag forwarder alicehua11/forwarder:latest
docker push alicehua11/forwarder:latest
