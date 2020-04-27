from blinkt import set_pixel, set_brightness, set_clear_on_exit, show, clear
from picamera import PiCamera
from random import randint
from time import sleep

def light_up():
  for pixel in range(8):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    set_pixel(pixel, r, g, b)
    show()
    sleep(0.1)

  sleep(1)
  clear()
  # must call this to turn lights off
  show()

set_brightness(0.2)
set_clear_on_exit()

SLEEP_TIME = 60 * 60 * 2

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

sleep(2)

for filename in camera.capture_continuous('/home/pi/time-lapse/img{counter:03d}.jpg'):
  light_up()
  sleep(SLEEP_TIME)
