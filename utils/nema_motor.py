from enum import IntEnum
import RPi.GPIO as GPIO
import time

class Rotation(IntEnum):
    CW = 0
    CCW = 1

class NMotor:
    def __init__(self, step_pin, dir, en_pin):
        self.STEP = step_pin # Step GPIO Pin
        self.DIR = dir # Direction GPIO Pin
        self.EN = en_pin # Enable GPIO Pin
        self.SPR = 200 # Steps per Revolution (360 / 7.5)
        self.delay = .0010
        self.enabled = True
        self.rotation = Rotation.CW
        
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.EN, GPIO.OUT)
        GPIO.output(self.DIR, GPIO.LOW) # LOW = clockwise, HIGH = counter-clockwise
        GPIO.output(self.EN, GPIO.HIGH) # HIGH = enabled, LOW = disabled
        
    def rotate_cw(self, step_count):
        self.rotation = Rotation.CW
        GPIO.output(self.DIR, GPIO.LOW)
        for x in range(step_count):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.delay)
            
    def rotate_ccw(self, step_count):
        self.rotation = Rotation.CCW
        GPIO.output(self.DIR, GPIO.HIGH)
        for x in range(step_count):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.delay)
            
    def enable(self):
        GPIO.output(self.EN, GPIO.HIGH)
        self.enabled = True
        
    def disable(self):
        GPIO.output(self.EN, GPIO.LOW)
        self.enabled = False
        