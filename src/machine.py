from utils.firebase import upload_file_to_firebase
from utils.notion import create_notion_entry
from utils.model import predict_type

from utils.lcd_display import LcdModule
from utils.stepper_motor import SMotorModule

import drivers
import time
import sys

import RPi.GPIO as GPIO
from utils.states import State

class JunkJudge:
    def __init__(self, lcd, motor, camera, led_red, led_green) -> None:
        self.lcd = lcd
        self.motor = motor
        self.camera = camera
        self.state = State.INIT
        self.led_red = led_red
        self.led_green = led_green

    def init(self):
        self.lcd.display("Initializing...")
        GPIO.setup(self.led_green, GPIO.OUT)
        GPIO.output(self.led_green, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.led_green, GPIO.LOW)
        self.state = State.IDLE
        self.lcd.display("Ready to go!")
    
    def update(self):  
        while True:
            try:
                # do something
                pass
            except KeyboardInterrupt:
                GPIO.cleanup()
                sys.exit()
