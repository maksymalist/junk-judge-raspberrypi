from picamera import PiCamera

camera = PiCamera()
PATH = '../images/image.jpg'

def take_picture():
    camera.capture(PATH)