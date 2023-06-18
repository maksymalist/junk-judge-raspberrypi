from picamera import PiCamera
import os

camera = PiCamera()
PATH = '../images/image.jpg'

def take_picture():
    print(os.getcwd())
    camera.capture(PATH)