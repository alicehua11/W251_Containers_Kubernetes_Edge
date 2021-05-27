docker build -t detector --no-cache .
docker tag detector alicehua11/detector:latest
docker push alicehua11/detector:latest
