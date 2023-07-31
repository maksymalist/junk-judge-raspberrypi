from utils.firebase import upload_file_to_firebase
from utils.notion import create_notion_entry
from utils.model import predict_type
from utils.confusion import get_confusion_level

import drivers
import time
import sys

import RPi.GPIO as GPIO
from utils.states import State

class JunkJudge:
    def __init__(self, lcd, motor, camera, led_red, led_green, trapdoor, recycle_override, trash_override, biological_override) -> None:
        self.lcd = lcd
        self.motor = motor
        self.camera = camera
        self.state = State.INIT
        self.led_red = led_red
        self.led_green = led_green
        self.trapdoor = trapdoor
        self.recycle_override = recycle_override
        self.trash_override = trash_override
        self.biologics_override = biological_override
        self.is_open = False
        
    def clear_all(self):
        #clear lcd and leds
        self.lcd.clear()
        self.led_green.off()
        self.led_red.off()
        
    def setup(self):
        # events for buttons

        ## Trapdoor ##
        self.trapdoor.press_event(self.toggle_open)
        
        #setup lcd and leds
        self.clear_all()
        self.lcd.setup_custom_characters()
        

    def init_sequence(self):
        self.clear_all()
        self.state = State.INIT
         
        self.lcd.display("Initializing...")
 
        for _ in range(3):
            self.led_green.on()
            time.sleep(0.5)
            self.led_green.off()
            time.sleep(0.5)
                
        self.lcd.display("Ready to go!")
        time.sleep(1)
        self.idle_sequence()
        
    def idle_sequence(self):
        self.clear_all()
        self.is_open = False
        print("idle sequence")
        print(self.is_open == True)
        self.state = State.IDLE
        self.lcd.display("# Open me #")
        self.led_green.on()
        
    def open_sequence(self):
        self.clear_all()
        self.led_green.on()
        self.lcd.display("# Insert Junk #", 1)
        
    def active_sequence(self):
        self.clear_all()
        self.state = State.ACTIVE
        self.led_red.on()
        file_path = 'images/test.jpg'
        
        ## take picture ##
        self.lcd.display_progress(0, "taking picture...")
        self.camera.take_picture(file_path)
        
        ## predict type ##
        self.lcd.display_progress(25, "Identifying type...")
        print("predicting type...")
        
        data = predict_type(file_path)
        prediction = data['result'][0]['result']
        
        #TODO: create a function to get the confusion level from the data
        confusion = get_confusion_level(data)
        
        ## upload to firebase ##
        self.lcd.display_progress(50, "Saving results...")
        key, file_size, file_type, file_name, file_url = upload_file_to_firebase(file_path, prediction)
        create_notion_entry(file_url, prediction, file_type, file_size, key)
        
        ## move motor ##
        self.lcd.display_progress(75, "Sorting junk...")
        
        print("*motor noises*")
        print("*motor noises*")
        print("*motor noises*")
        
        ## switch to success mode ##
        self.lcd.display_progress(100, "Done !")
        time.sleep(1)
        self.success_sequence()
        
    def success_sequence(self):
        self.clear_all()
        self.led_green.on()
        self.lcd.display("Thanks for saving", 1)
        self.lcd.display("the planet :)", 2)
        time.sleep(2)
        self.idle_sequence()
        
    def failure_sequence(self):
        self.clear_all()
        self.led_red.on()
        self.lcd.display("Something went", 1)
        self.lcd.display("wrong :(", 2)
        time.sleep(2)
        self.init_sequence()
        
        
    
    def on_update(self):  
        pass
    
    def toggle_open(self, channel):
        print("button pressed")
        print(self.is_open == True)
        
        if self.state != State.IDLE:
            return 
        
        if self.is_open:
            self.active_sequence()
            self.is_open = False
        else:
            self.open_sequence()
            self.is_open = True
            
