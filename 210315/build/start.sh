#!/bin/sh

echo "Building time_messenger docker"
docker build -f ./build/docker/Dockerfile -t time_messenger ./build/docker/

echo "Starting time_messenger docker"
docker run --rm -d \
    -v $(pwd)/sources:/home/time_messenger/bin \
    -v $(pwd)/data:/home/time_messenger/data \
    -p 8012:8000 \
    time_messenger
