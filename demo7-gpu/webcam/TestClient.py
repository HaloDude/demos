import cv2
import numpy as np
import requests
import json
import jsonpickle
import jsonpickle.ext.numpy as jsonpickle_numpy
jsonpickle_numpy.register_handlers()



addr = 'http://localhost:8010/'
content_type = 'image/jpeg'
headers = {'content-type': content_type}

response = requests.get(addr)

while True:
    frame = np.fromstring(response.content, np.uint8)

    img = cv2.imdecode(frame, cv2.IMREAD_COLOR)

    if img is not None:
        cv2.imshow('image', img)
        cv2.waitKey(1)

    response = requests.get(addr)





# while True:
#     print(response.text)
#     # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
#     # cv2.imshow('frame', gray)
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break
#
#     response = requests.get(addr)
