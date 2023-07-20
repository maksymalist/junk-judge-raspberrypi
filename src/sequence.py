import RPi.GPIO as GPIO
from utils.led import LED
from utils.button import Button
import time

from utils.states import State
    

def init_mode(machine, lcd, led_green):
    lcd.display("Initializing...")
 
    for _ in range(3):
        led_green.on()
        time.sleep(0.5)
        led_green.off()
        time.sleep(0.5)
            
        machine.state = State.IDLE
        machine.lcd.clear()
        lcd.display("Ready to go!")
        time.sleep(1)

def idle_mode(lcd, led_green):
    lcd.display("Insert Junk")
    led_green.on()
    
    
def active_mode(lcd, led_red):
    led_red.on()
    
    steps = [
        {
            "message": "Taking picture...",
            "progress": 0,
        },
        {
            "message": "Identifying type...",
            "progress": 25,
        },
        {
            "message": "Sorting junk...",
            "progress": 50,
        },
        {
            "message": "Sorting junk...",
            "progress": 75,
        },
        {
            "message": "Done !",
            "progress": 100,
        }
    ]
    
    lcd.display_progress(steps)
    
    
