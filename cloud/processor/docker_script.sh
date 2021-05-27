docker build -t processor --no-cache .
docker tag processor alicehua11/processor:latest
docker push alicehua11/processor:latest
