from time import sleep
from picamera import PiCamera

SLEEP_TIME = 60 * 60 * 2

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

sleep(2)

for filename in camera.capture_continuous('/home/pi/time-lapse/img{counter:03d}.jpg'):
  sleep(SLEEP_TIME)
