from enum import Enum
import RPi.GPIO as GPIO
import time

class Rotation(Enum):
    CW = 1
    CCW = 0

    def __str__(self) -> str:
        return self.value

class NMotor:
    def __init__(self, dir, step_pin):
        self.DIR = dir # Direction GPIO Pin
        self.STEP = step_pin # Step GPIO Pin
        self.SPR = 48 # Steps per Revolution (360 / 7.5)
        self.rotation = Rotation.CW # Clockwise Rotation
        self.delay = .0208
        
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.output(self.DIR, self.rotation.value)
        
    def rotate_cw(self, step_count):
        self.rotation = Rotation.CW
        GPIO.output(self.DIR, self.rotation.value)
        for x in range(step_count):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.delay)
            
    def rotate_ccw(self, step_count):
        self.rotation = Rotation.CCW
        GPIO.output(self.DIR, self.rotation.value)
        for x in range(step_count):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.delay)