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
    def __init__(self, dir_pin, en_pin, step_pin, delay):
        self.dir_pin = dir_pin
        self.en_pin = en_pin
        self.step_pin = step_pin
        self.delay = delay
        
        GPIO.setup(self.pins, GPIO.OUT)
        
        
        
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     200, # number of steps
                     .0005, # step delay [sec]
                     False, # True = print verbose output 
                     .05) # initial delay [sec]

GPIO.cleanup() # clear GPIO allocations after run