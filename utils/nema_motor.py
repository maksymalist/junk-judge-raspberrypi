from enum import IntEnum
import RPi.GPIO as GPIO
import time

class Rotation(IntEnum):
    CW = 1
    CCW = 0

class NMotor:
    def __init__(self, dir, step_pin):
        self.DIR = dir # Direction GPIO Pin
        self.STEP = step_pin # Step GPIO Pin
        self.SPR = 200 # Steps per Revolution (360 / 7.5)
        self.delay = .0045
        
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.EN, GPIO.OUT)
        
    def rotate_cw(self, step_count):
        GPIO.output(self.DIR, Rotation.CW)
        for x in range(step_count):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.delay)
            
    def rotate_ccw(self, step_count):
        self.rotation = Rotation.CCW
        GPIO.output(self.DIR, Rotation.CW)
        for x in range(step_count):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.delay)