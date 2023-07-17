from utils.firebase import upload_file_to_firebase
from utils.notion import create_notion_entry
from utils.model import predict_type

from utils.lcd_display import LcdModule
from utils.stepper_motor import SMotorModule

from src.lcd_sequence import idle_mode

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
        
        # clear lcd and leds
        self.lcd.clear()
        GPIO.setup(self.led_red, GPIO.OUT)
        GPIO.setup(self.led_green, GPIO.OUT)
        
        GPIO.output(self.led_red, GPIO.LOW)
        GPIO.output(self.led_green, GPIO.LOW)
        
        self.lcd.display("Initializing...")
 
        for i in range(3):
            GPIO.output(self.led_green, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self.led_green, GPIO.LOW)
            time.sleep(1)
            
        self.state = State.IDLE
        self.lcd.clear()
        self.lcd.display("Ready to go!")
        time.sleep(1)
        
        idle_mode(self.lcd, self.led_green)
    
    def update(self):  
        while True:
            try:
                # do something
                pass
            except KeyboardInterrupt:
                GPIO.cleanup()
                sys.exit()
