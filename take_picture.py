from blinkt import set_pixel, set_brightness, set_clear_on_exit, show
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

set_brightness(0.2)
set_clear_on_exit()

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

file_name = input('What would you like to call this image? ')

light_up()
camera.capture(file_name + '.jpg')
