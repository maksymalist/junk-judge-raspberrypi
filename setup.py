# from utils.firebase import upload_file_to_firebase
# from utils.notion import create_notion_entry
# from utils.model import predict_type
from picamera import PiCamera
from utils.lcd_display import LcdModule
from utils.stepper_motor import SMotorModule
from utils.camera import CameraModule
from utils.led import LED
from utils.button import Button
from src.machine import JunkJudge

import firebase_admin
from firebase_admin import credentials
import drivers
import sys
import RPi.GPIO as GPIO
import atexit

if __name__ == "__main__":

    try:
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'junk-judge.appspot.com'
        })

        
        camera = PiCamera()
        screen = drivers.Lcd()
        
        camera_module = CameraModule(camera, (500, 500), 50)
        lcd_module = LcdModule(screen)
        stepper_motor_module = None #SMotorModule(22, 23, 24, (21,21,21))
        
        led_red = LED(38)
        led_green = LED(40)
        
        trapdoor_open  = Button(16)
        trapdoor_close = Button(18)
        
        recycle_override = Button(22)
        trash_override = Button(32)
        biologics_override = Button(36)
        
        
        machine = JunkJudge(
            lcd_module, 
            stepper_motor_module, 
            camera_module, 
            led_red, 
            led_green, 
            trapdoor_open, 
            trapdoor_close,
            recycle_override, 
            trash_override, 
            biologics_override
            )
        
        machine.setup()
        machine.motor_test()
        # machine.init_sequence()
        
        atexit.register(machine.clear_all)
        # atexit.register(machine.turn_off)
        
        # while True:
        #     machine.on_update()
        

    except KeyboardInterrupt:
        GPIO.cleanup()
        machine.clear_all()
        sys.exit()
        
    except Exception as e:
        print("failed to do something", e)
        #machine.failure_sequence()





    # file_path = 'images/test.jpg'
    # prediction = predict_type(file_path)
    # key, file_size, file_type, file_name, file_url = upload_file_to_firebase(file_path, prediction)

    # print('File uploaded successfully.')
    # print('File Size:', file_size)
    # print('File Type:', file_type)
    # print('File Name:', file_name)
    # print('File URL:', file_url)
    
    #print(create_notion_entry(file_url, prediction, file_type, file_size, key))

    
    # on start
    
