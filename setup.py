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
        stepper_motor_module = SMotorModule((29,31,33,35), 0.002)
        
        led_red = LED(38)
        led_green = LED(40)
        
        trapdoor = Button(18)
        recycle_override = Button(22)
        trash_override = Button(32)
        biologics_override = Button(36)
        
        
        machine = JunkJudge(
            lcd_module, 
            stepper_motor_module, 
            camera_module, 
            led_red, 
            led_green, 
            trapdoor, 
            recycle_override, 
            trash_override, 
            biologics_override
            )
        
        machine.setup()
        machine.init_sequence()
        
        while True:
            machine.on_update()
        

    except KeyboardInterrupt:
        GPIO.cleanup()
        machine.clear_all()
        sys.exit()
        
    except Exception as e:
        print("failed to do something")
        machine.failure_sequence()





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
    
