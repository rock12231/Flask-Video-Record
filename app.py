from flask import Flask, render_template, Response, redirect, url_for
import cv2
import threading
import time

app = Flask(__name__)

# Global variables
capture = False
out = None
frame_width = 640
frame_height = 480
fps = 20.0
video_file = 'static/recorded_video.mp4'

# Video capture object
cap = cv2.VideoCapture(0)

# Function to capture video
def capture_video():
    global capture, out
    while capture:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_capture')
def start_capture():
    global capture, out
    capture = True
    out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
    
    # Start the video capture in a new thread
    capture_thread = threading.Thread(target=capture_video)
    capture_thread.start()
    
    return redirect(url_for('index'))

@app.route('/stop_capture')
def stop_capture():
    global capture
    capture = False
    return redirect(url_for('index'))

@app.route('/play_video')
def play_video():
    return render_template('play_video.html', video_file=video_file)

# Stream the camera feed
def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/auto_play')
def auto_play():
    return redirect(url_for('play_video'))

if __name__ == "__main__":
    app.run(debug=True)
