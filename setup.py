from utils.firebase import upload_file_to_firebase
from utils.notion import create_notion_entry
from utils.model import predict_type

from src.lcd_display import LcdModule
from src.stepper_motor import SMotorModule

import drivers
import time
import sys

import RPi.GPIO as GPIO

if __name__ == "__main__":

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # file_path = 'images/test.jpg'
    # prediction = predict_type(file_path)
    # key, file_size, file_type, file_name, file_url = upload_file_to_firebase(file_path, prediction)

    # print('File uploaded successfully.')
    # print('File Size:', file_size)
    # print('File Type:', file_type)
    # print('File Name:', file_name)
    # print('File URL:', file_url)

    screen = drivers.Lcd()
    lcd = LcdModule(screen)
    lcd.display("hello gigga")

    channels = (29,31,33,35)
    wait_time = 0.002

    motor = SMotorModule(channels, wait_time)
    motor.setup()

    ang = 5200

    motor.rotate_clockwise(ang)

    #print(create_notion_entry(file_url, prediction, file_type, file_size, key))
