# It need tensor flow gpu support 
#FROM tensorflow/tensorflow:latest-gpu

# if just need cuda
FROM nvidia/cuda
LABEL maintainer dfedorchuk@eashbanctech.com


RUN apt-get update && apt-get install -y python-pip && \
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E1DD270288B4E6030699E45FA1715D88E1DF1F24 && \
su -c "echo 'deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main' > /etc/apt/sources.list.d/git.list" && \
apt-get update  && \
apt-get install -y git

RUN apt-get install -y nano && \
apt-get install wget


RUN apt-get install -y libglib2.0-0 && \
apt-get install -y libsm6 && \
apt-get install libxrender1



RUN pip install opencv-contrib-python==3.4.0.12 && \
pip install youtube-dl && \
pip install flask && \
pip install requests


USER root
EXPOSE 8005
WORKDIR /opt

COPY /darknet /opt/darknet
COPY run.sh /opt

RUN chmod +x /opt/run.sh

ENV VIDEO_LINK=https://www.youtube.com/watch?v=9bZkp7q19f0
ENV VIDEO_OUTPUT_COMPRESSION=10
ENV OUTPUT_PORT=8005
ENV CAM=0

CMD ["./run.sh"]


# To run the sshuttle 
# sshuttle --no-latency-control -N -v -r user@ip localhost:8000 localhost:8000

#docker pull dfedorchuk/qb_ebt:nvidia_demo
#nvidia-docker run -p 8000:8000 dfedorchuk/qb_ebt:nvidia_demo

# SSh tunnel
# ssh -i "dfedorchuk.pem" -L 8010:127.0.0.1:8010 -L 8005:127.0.0.1:8005 ubuntu@ec2-34-204-166-136.compute-1.amazonaws.com -N
