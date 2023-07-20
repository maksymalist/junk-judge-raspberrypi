import RPi.GPIO as GPIO
from utils.led import LED
from utils.button import Button
import time
    

def idle_mode(lcd, led_green):
    lcd.clear()
    lcd.display("Insert Junk")
    led_green.on()
    
    
def active_mode(lcd, led_red):
    lcd.clear()
    lcd.display_progress()
    led_red.on()
