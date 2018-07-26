#!/usr/bin/env bash
sudo docker build -t gpu ../demo7-gpu
sudo nvidia-docker run -it --net host -p 8005:8005 --env OUTPUT_PORT=8005 --env CAM=0 --env VIDEO_LINK=https://www.youtube.com/watch?v=9bZkp7q19f0 gpu