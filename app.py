from flask import Flask, render_template, Response
from camera import Video

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')

def video():
    return Response(gen(Video("video1.mp4")),
    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video1')
def video1():
    return Response(gen(Video("video2.mp4")),
    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video2')
def video2():
    return Response(gen(Video("video3.mp4")),
    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video3')
def video3():
    return Response(gen(Video("video4.mp4")),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug = True)