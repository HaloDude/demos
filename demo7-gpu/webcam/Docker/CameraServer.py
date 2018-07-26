import sys
from flask import Flask, request, Response

app = Flask(__name__)

video_frames = []


@app.route('/', methods=['GET'])
def getImg():
    if len(video_frames) > 0:
        img = video_frames.pop(0)

        return Response(response=img, status=200, mimetype='application/text')
    else:
        return Response(status=206)


@app.route('/', methods=['POST'])
def postImg():
    r = request

    if len(video_frames) < 400:
        video_frames.append(r.data)
        print('Got frame: ', len(video_frames))
    else:
        print('Overflow')
        video_frames.pop(0)
        video_frames.append(r.data)

    return Response(status=200)


if __name__ == "__main__":
    port = int(sys.argv[1])

    app.run(host="127.0.0.1", port=port)
