from utils.firebase import upload_file_to_firebase
from utils.notion import create_notion_entry
from utils.model import predict_type

from utils.lcd_display import LcdModule
from utils.stepper_motor import SMotorModule

from src.sequence import init_mode, idle_mode, active_mode

import drivers
import time
import sys

import RPi.GPIO as GPIO
from utils.states import State

class JunkJudge:
    def __init__(self, lcd, motor, camera, led_red, led_green, trapdoor) -> None:
        self.lcd = lcd
        self.motor = motor
        self.camera = camera
        self.state = State.INIT
        self.led_red = led_red
        self.led_green = led_green
        self.trapdoor = trapdoor
        self.is_open = False
        self.debug = False

    def on_init(self):
        
        # events for buttons

        ## Trapdoor ##
        self.trapdoor.press_event(self.toggle_open)
        
        #clear lcd and leds
        self.lcd.clear()
        self.lcd.setup_custom_characters()
        self.led_green.off()
        self.led_red.off()
        
        if not self.debug:
            init_mode(self, self.lcd, self.led_green)
        
        
        idle_mode(self.lcd, self.led_green)
        # self.motor.setup()
        # self.motor.rotate_clockwise(10000)
    
    def on_update(self):  
        pass
            
    
    def toggle_open(self, channel):
        
        if self.state != State.IDLE:
            return 
        
        self.is_open = not self.is_open
        
        if self.is_open:
            active_mode(self.lcd, self.led_red)
            self.state = State.ACTIVE

