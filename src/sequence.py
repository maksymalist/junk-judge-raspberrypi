import RPi.GPIO as GPIO
from utils.led import LED
from utils.button import Button
import time
    

def idle_mode(lcd, led_green):
    lcd.clear()
    lcd.display("insert junk")
    led_green.on()