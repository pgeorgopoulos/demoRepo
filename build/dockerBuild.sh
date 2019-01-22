#!/bin/bash -xe

docker build . --build-arg APPENV=$APPENV -t amneok/flaskapp3:v$BUILD_ID
docker push amneok/flaskapp3:v$BUILD_ID
