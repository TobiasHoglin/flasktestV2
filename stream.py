# stream.py

import io
import picamera2
import time
from picamera2.encoders import MJPEGEncoder
from picamera2.outputs import PiCameraCircularIO

def generate_frames():
    camera = picamera2.PiCamera()

    # Configure camera settings (e.g., resolution)
    camera.resolution = (640, 480)
    camera.framerate = 30

    # Create a circular buffer to store video
    circular_buffer = PiCameraCircularIO(camera, seconds=10)

    # Start recording
    camera.start_recording(circular_buffer, format='mjpeg')

    try:
        while True:
            # Wait for the next frame
            camera.wait_recording(0.1)

            # Yield the current frame
            yield (b'--FRAME\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + circular_buffer.read1() + b'\r\n')

    finally:
        camera.stop_recording()

if __name__ == "__main__":
    app.run()
