from PIL import Image


class CameraModule:
    def __init__(self, picamera, img_size, img_quality) -> None:
        self.camera = picamera
        self.img_size = img_size
        self.img_quality = img_quality

    def take_picture(self, output):
        self.camera.capture(output)
        self.optimize_image(output, self.img_size, self.img_quality)

    def optimize_image(self, input_path, size, quality):
        img = Image.open(input_path)
        img = img.resize(size)  # Resize the image to the desired dimensions
        img.save(input_path, optimize=True, quality=quality)  # Compress and save the image


