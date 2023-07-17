import RPi.GPIO as GPIO
from utils.led import LED
from utils.button import Button
import time

def callback():
    led = LED(38)
    led.on()
    time.sleep(1)
    led.off()
    
    

def idle_mode(lcd, led_green):
    lcd.clear()
    lcd.display("insert junk")
    led_green.on()
    
    button = Button(22)
    print("button pressed")
    button.press_event(callback)
    