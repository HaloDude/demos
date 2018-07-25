import numpy as np
import cv2
import sys
from threading import Thread
from flask import Flask, render_template, Response
import time
import socket
import jsonpickle
import json

app = Flask(__name__)

video_frames = []
class CamThread(Thread):
    def __init__(self, cap, bufferSize):
        Thread.__init__(self)
        self.sleep = float(1 / 60)
        self.running = True
        self.cap = cap
        self.bufferSize = bufferSize

    def run(self):
        global video_frames

        while self.running:
            ret, frame = cap.read()
            print type(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
            #cv2.imshow('frame', gray)
            if not ret:
                print "Cam is off or broken."
                self.running = False
                break

            # Refresh screen. Dont need it really
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

            if len(video_frames) < self.bufferSize:
                # Save frame for processing
                video_frames.append(frame)
                print "Frame added: ", len(video_frames)
            else:
                # Buffer overflow. Remove front, add to back
                video_frames.pop(0)
                video_frames.append(frame)
                print "Buffer overflow: ", len(video_frames)

            # Sleep
            time.sleep(self.sleep)


@app.route('/', methods=['GET'])
def getImg():
    if len(video_frames) > 0:
        img = video_frames.pop(0)
        _, img = cv2.imencode('.jpg', img)

        return Response(response=img.tostring(), status=200, mimetype='application/text')


if __name__ == "__main__":

    threads = []
    #port = int(sys.argv[1])

    cap = cv2.VideoCapture(0)
    read_cam_tread = CamThread(cap, 400)
    read_cam_tread.deamon = True
    read_cam_tread.start()
    threads.append(read_cam_tread)

    app.run(host="192.168.0.110", port=8010)

    def has_live_threads(threads):
        return True in [t.isAlive() for t in threads]


    while has_live_threads(threads):
        try:
            # synchronization timeout of threads kill
            [t.join(1) for t in threads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            # Ctrl-C handling and send kill to threads
            print "Sending kill to threads..."
            for t in threads:
                t.running = False
    print "Exited"

    cap.release()
    cv2.destroyAllWindows()