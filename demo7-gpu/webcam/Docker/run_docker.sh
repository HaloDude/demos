#!/usr/bin/env bash
sudo docker build -t webcam_server ../Docker
sudo docker run -it --net host -p 8010:8010 --env OUTPUT_PORT=8010 webcam_server