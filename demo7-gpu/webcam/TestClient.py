import cv2
import requests
from threading import Thread
import time


addr = 'http://127.0.0.1:8011/'
content_type = 'application/text'
headers = {'content-type': content_type}


class CamThread(Thread):
    def __init__(self, cap, bufferSize):
        Thread.__init__(self)
        self.sleep = float(1 / 60)
        self.running = True
        self.cap = cap
        self.bufferSize = bufferSize

    def run(self):
        while self.running:
            ret, frame = cap.read()
            _, img = cv2.imencode('.jpg', frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if not ret:
                print "Cam is off or broken."
                self.running = False
                break

            res = requests.post(addr, data=img.tostring(), headers=headers)

            # Sleep
            time.sleep(self.sleep)


if __name__ == '__main__':
    threads = []
    cap = cv2.VideoCapture(1)
    read_cam_tread = CamThread(cap, 400)
    read_cam_tread.deamon = True
    read_cam_tread.start()
    threads.append(read_cam_tread)


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


#
# response = requests.get(addr)
#
# while True:
#     frame = np.fromstring(response.content, np.uint8)
#
#     img = cv2.imdecode(frame, cv2.IMREAD_COLOR)
#
#     if img is not None:
#         cv2.imshow('image', img)
#         cv2.waitKey(1)
#
#     response = requests.get(addr)





# while True:
#     print(response.text)
#     # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
#     # cv2.imshow('frame', gray)
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break
#
#     response = requests.get(addr)
