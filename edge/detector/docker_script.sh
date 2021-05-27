docker build -t detector --no-cache .
docker tag detector alicehua11/detector:v1
docker push alicehua11/detector:v1
