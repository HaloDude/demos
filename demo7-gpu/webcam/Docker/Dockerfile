FROM ubuntu

RUN apt-get update && \
  apt-get install -y python3 python3-pip && \
rm -rf /var/lib/apt/lists/*

RUN pip3 install flask && \
pip3 install requests

COPY CameraServer.py /opt
COPY run.sh /opt

USER root
EXPOSE 8010

RUN chmod +x /opt/run.sh

ENV OUTPUT_PORT=8010

CMD ["./opt/run.sh"]

