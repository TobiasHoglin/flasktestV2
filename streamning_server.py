from flask import Flask, render_template, Response
from stream_test_lib import * 

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def video_feed():
    return Response(stream.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=FRAME')

if __name__ == "__main__":
    app.run()
