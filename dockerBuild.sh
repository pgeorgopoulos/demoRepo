#!/bin/bash -xe

APPENV="$1"
BUILD_ID="$2"

docker build . --build-arg APPENV=$APPENV -t amneok/flaskapp3:v$BUILD_ID
docker push amneok/flaskapp3:v$BUILD_ID
