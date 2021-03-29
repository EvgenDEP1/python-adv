#!/bin/sh

echo "Starting time_messenger docker"
docker run --rm -it \
    -v $(pwd)/sources:/home/time_messenger/bin \
    -v $(pwd)/data:/home/time_messenger/data \
    -p 8012:8000 \
    time_messenger sh

