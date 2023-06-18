from picamera import PiCamera
import os

camera = PiCamera()
PATH = 'image.jpg'

def take_picture():
    camera.capture(PATH)