from picamera import PiCamera
from PIL import Image
import os

camera = PiCamera()

def resize_and_compress_image(input_path, size, quality):
    img = Image.open(input_path)
    img = img.resize(size)  # Resize the image to the desired dimensions
    img.save(input_path, optimize=True, quality=quality)  # Compress and save the image

def take_picture(output):
    camera.capture(output)
    resize_and_compress_image(output, (224, 224), 70)