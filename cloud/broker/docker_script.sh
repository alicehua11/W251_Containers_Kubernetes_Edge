docker build -t broker --no-cache .
docker tag broker alicehua11/broker:latest
docker push alicehua11/broker:latest
