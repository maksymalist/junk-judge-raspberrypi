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
    
    # step 1: take picture of junk
    lcd.display_progress(0, "Taking picture...")
    lcd.clear()
    time.sleep(2)
    
    # step 2: predict type of junk
    lcd.display_progress(25, "identifying type...")
    lcd.clear()
    time.sleep(2)
    
    # step 3: upload to firebase
    lcd.display_progress(50, "Sorting junk...")
    lcd.clear()
    time.sleep(2)
    
    # step 4: sort junk
    lcd.display_progress(75, "Sorting junk...")
    lcd.clear()
    time.sleep(2)
    
    # step 5: done
    lcd.display_progress(100, "Done !")
    lcd.clear()
    time.sleep(2)
    
    
