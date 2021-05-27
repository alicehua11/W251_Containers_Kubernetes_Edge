docker build -t logger --no-cache .
docker tag logger alicehua11/logger:latest
docker push alicehua11/logger:latest
