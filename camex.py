import picamera
import time

def run():
  camera = picamera.PiCamera()
  camera.capture('example.jpg')

#  camera.vflip = True

#  camera.capture('example2.jpg')

#  camera.start_recording('examplevid.h264')
#  time.sleep(10)
#  camera.stop_recording()

if __name__ == '__main__':
  run()
