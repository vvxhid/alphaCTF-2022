#! /bin/bash

docker build -t preserve-backup  .
docker ps -a | grep preserve-backup | awk '{ print $1}' | xargs docker rm --force 2> /dev/null

docker run --name "preserve-backup-container" -p 0.0.0.0:9001:9001/tcp -d -t preserve-backup