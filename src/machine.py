from utils.firebase import upload_file_to_firebase
from utils.notion import create_image_entry, update_judge_status
from utils.model import predict_type
from utils.confusion import get_confusion_level

import drivers
import time
import sys

import RPi.GPIO as GPIO
from utils.states import State

class JunkJudge:
    def __init__(self, lcd, motor, camera, led_red, led_green, trapdoor_open, trapdoor_close, recycle_override, trash_override, biological_override) -> None:
        self.version = "Beta v1.0"
        self.judge_id = 1
        self.loop_count = 0
        self.lcd = lcd
        self.motor = motor
        self.camera = camera
        self.state = State.INIT
        self.led_red = led_red
        self.led_green = led_green
        self.trapdoor_open = trapdoor_open
        self.trapdoor_close = trapdoor_close
        self.recycle_override = recycle_override
        self.trash_override = trash_override
        self.biologics_override = biological_override
        self.is_item = False

        
    def clear_all(self):
        #clear lcd and leds
        self.lcd.clear()
        self.led_green.off()
        self.led_red.off()
        
    def setup(self):  
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
        self.is_item = False
        print("idle sequence")
        self.state = State.IDLE
        self.lcd.display("#   Open me!   #")
        self.led_green.on()
        
    def open_sequence(self):
        self.clear_all()
        self.led_green.on()
        self.lcd.display("# Insert Trash #", 1)
        
    def active_sequence(self):
        self.clear_all()
        self.state = State.ACTIVE
        self.led_red.on()
        file_path = 'images/test.jpg'
        
        ## take picture ##
        self.lcd.display_progress(0, "Scanning...")
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
        create_image_entry(file_url, prediction, file_type, file_size, key)
        
        ## move motor ##
        self.lcd.display_progress(75, "Sorting...")
        
        print("*motor noises*")
        print("*motor noises*")
        print("*motor noises*")
        
        time.sleep(1)
        
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
        
        
    # def turn_off(self):
    #     update_judge_status(
    #         self.judge_id, 
    #         str(self.trapdoor_open.is_pressed()),
    #         "Off",  ## <---- Triggers when the program is turned off
    #         str(self.state),
    #         self.version
    #     )
        
        
    
    def on_update(self):  
        
        # # Status update
        # if self.loop_count % 100 == 0:
        #     update_judge_status(
        #         self.judge_id, 
        #         str(self.trapdoor_open.is_pressed()),
        #         "On",   ## <---- reaffirming that the machine is on
        #         str(self.state),
        #         self.version
        #     )
        
        
        # Button sequence
        if self.state == State.IDLE:
            if self.trapdoor_open.is_pressed() and not self.is_item:
                self.open_sequence()
                self.is_item = True
            elif self.trapdoor_close.is_pressed() and self.is_item:
                self.active_sequence()
                
        self.loop_count += 1

            
