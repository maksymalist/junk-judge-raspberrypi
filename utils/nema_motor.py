import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

direction= 22 # Direction (DIR) GPIO Pin
step = 23 # Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

###########################
# Actual motor control
###########################
#

class NMotor:
    def __init__(self, dir_pin, step_pin, enable_pin, motor_pins):
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        self.enable_pin = enable_pin
        self.motor_pins = motor_pins
        self.motor = RpiMotorLib.A4988Nema(dir_pin, step_pin, motor_pins, "DRV8825")
        
        GPIO.setup(enable_pin, GPIO.OUT)
        
    def rotate(self, direction, num_steps=200):
        GPIO.output(self.enable_pin, GPIO.LOW)
        self.motor.motor_go(direction, # False=Clockwise, True=Counterclockwise
            "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
            num_steps, # number of steps
            .0005, # step delay [sec]
            False, # True = print verbose output 
            .05) # initial delay [sec]
        GPIO.output(self.enable_pin, GPIO.HIGH)