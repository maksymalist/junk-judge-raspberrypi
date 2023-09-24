from utils.firebase import upload_file_to_firebase
from utils.notion import create_image_entry
from utils.model import predict_type
from utils.confusion import get_confusion_level

import time
from utils.states import State
from utils.languages import Language, language_dict

class JunkJudge:
    def __init__(self, language=Language.EN, lcd=None, conveyor_1=None, camera=None, led_red=None, led_green=None, trapdoor_open=None, trapdoor_close=None) -> None:
        self.version = "Beta v1.0"
        self.language = language
        self.translations = language_dict[self.language.value]
        self.judge_id = 1
        self.lcd = lcd
        self.conveyor_1 = conveyor_1
        self.camera = camera
        self.state = State.INIT
        self.led_red = led_red
        self.led_green = led_green
        self.trapdoor_open = trapdoor_open
        self.trapdoor_close = trapdoor_close
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
        print("INIT sequence \n")
        self.clear_all()
        self.state = State.INIT
         
        self.lcd.display(self.translations["init"])
 
        for _ in range(3):
            self.led_green.on()
            time.sleep(0.5)
            self.led_green.off()
            time.sleep(0.5)
                
        self.lcd.display(self.translations["ready"])
        time.sleep(1)
        if self.trapdoor_open.is_pressed():
            self.open_sequence()
        else:
            self.idle_sequence()
        
    def idle_sequence(self):
        print("IDLE sequence \n")
        self.clear_all()
        self.is_item = False
        self.state = State.IDLE
        self.lcd.display(self.translations["idle"])
        self.led_green.on()
        
    def open_sequence(self):
        print("OPEN sequence \n")
        self.clear_all()
        self.is_item = False
        self.state = State.IDLE
        self.lcd.display(self.translations["opened"], 1)
        self.led_green.on()
        
    def active_sequence(self):
        print("ACTIVE sequence \n")
        
        self.clear_all()
        self.state = State.ACTIVE
        self.led_red.on()
        file_path = 'images/test.jpg'
        
        ## take picture ##
        self.lcd.display_progress(0, self.translations["active"]["scan"])
        self.camera.take_picture(file_path)
        
        ## predict type ##
        self.lcd.display_progress(25, self.translations["active"]["prediction"])
        print("Predicting type...")
        
        data = predict_type(file_path)
        prediction = data['result'][0]['result']
        
        #TODO: create a function to get the confusion level from the data
        confusion = get_confusion_level(data)
        
        ## upload to firebase ##
        self.lcd.display_progress(50, self.translations["active"]["save"])
        key, file_size, file_type, file_name, file_url = upload_file_to_firebase(file_path, prediction)
        create_image_entry(file_url, prediction, file_type, file_size, key)
        
        ## move motor ##
        self.lcd.display_progress(75, self.translations["active"]["sorting"])
        
        # add motor code here
        
        print("*motor noises*")
        print("*motor noises*")
        print("*motor noises*")
        
        time.sleep(1)
        
        ## switch to success mode ##
        self.lcd.display_progress(100, self.translations["active"]["done"])
        time.sleep(1)
        self.success_sequence()
        
    def success_sequence(self):
        print("SUCCESS sequence \n")
        
        self.clear_all()
        self.led_green.on()
        self.lcd.display(self.translations["success"]["top"], 1)
        self.lcd.display(self.translations["success"]["bottom"], 2)
        time.sleep(2)
        if self.trapdoor_open.is_pressed():
            self.open_sequence()
        else:
            self.idle_sequence()
        
    def failure_sequence(self):
        self.clear_all()
        self.led_red.on()
        self.lcd.display(self.translations["failure"]["top"], 1)
        self.lcd.display(self.translations["failure"]["bottom"], 2)
        time.sleep(2)
        self.init_sequence()
        
    def motor_sequence(self):
        self.conveyor_1.enable()
        self.conveyor_1.rotate_ccw(1000)
        self.conveyor_1.disable()
        time.sleep(5)
        self.conveyor_1.enable()
        self.conveyor_1.rotate_cw(1000)
        self.conveyor_1.disable()
        ##self.conveyor_1.rotate_ccw(100)
        
        
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

            
