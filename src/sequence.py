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
    
    
def active_mode(machine, lcd, led_red):
    led_red.on()
    
    lcd.display_progress(0, "taking picture...") ## take picture ##
    time.sleep(1)
    lcd.display_progress(25, "Identifying type...") ## predict type ##
    time.sleep(1)
    lcd.display_progress(50, "Saving results...")  ## upload to firebase ##
    time.sleep(1)
    lcd.display_progress(75, "Sorting junk...") ## move motor ##
    time.sleep(1)
    lcd.display_progress(100, "Done !") ## switch to success mode ##
    
    
