from utils.led import LED
from utils.button import Button
from utils.states import State

from utils.model import predict_type
from utils.firebase import upload_file_to_firebase
from utils.notion import create_notion_entry

import RPi.GPIO as GPIO
import time
    

def init_mode(machine, lcd, led_green):
    lcd.display("Initializing...")
 
    for _ in range(3):
        led_green.on()
        time.sleep(0.5)
        led_green.off()
        time.sleep(0.5)
            
        machine.clear_all()
        lcd.display("Ready to go!")
        time.sleep(1)
        machine.state = State.IDLE

def idle_mode(lcd, led_green):
    lcd.display("Insert Junk")
    led_green.on()
    
    
def active_mode(camera, lcd, led_red):
    led_red.on()
    file_path = 'images/test.jpg'
    
    ## take picture ##
    lcd.display_progress(0, "taking picture...")
    camera.take_picture(file_path)
    
    ## predict type ##
    lcd.display_progress(25, "Identifying type...")
    prediction = predict_type(file_path)
    
    ## upload to firebase ##
    lcd.display_progress(50, "Saving results...")
    key, file_size, file_type, file_name, file_url = upload_file_to_firebase(file_path, prediction)
    create_notion_entry(file_url, prediction, file_type, file_size, key)
    
    ## move motor ##
    lcd.display_progress(75, "Sorting junk...")
    print("*motor noises*")
    print("*motor noises*")
    print("*motor noises*")
    
    ## switch to success mode ##
    lcd.display_progress(100, "Done !")
    
def confused_mode(lcd, trash_override, recycle_override, biologics_override, led_red, led_green):
    lcd.display("I'm confused")
    led_red.on()