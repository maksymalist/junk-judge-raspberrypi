from picamera import PiCamera
from utils.lcd_display import LcdModule
from utils.nema_motor import NMotor
from utils.camera import CameraModule
from utils.led import LED
from utils.button import Button
from src.machine import JunkJudge
import time
import firebase_admin
from firebase_admin import credentials
import drivers
import sys
import RPi.GPIO as GPIO
import atexit

from utils.languages import Language

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
        
        camera_module = CameraModule(camera, (648, 486), 100)
        lcd_module = LcdModule(screen)  
        conveyor_module_1 = NMotor(29, 31, 33) # BCM 5, 6, 13 respectively
        conveyor_module_2 = NMotor(35, 37, 36) # BCM 19, 26, 16 respectively
        
        led_red = LED(38)
        led_green = LED(40)
        
        trapdoor_open  = Button(12)
        trapdoor_close = Button(16)
        
        machine = JunkJudge(
            language=Language.FR,
            lcd=lcd_module, 
            conveyor_1=conveyor_module_1, 
            conveyor_2=conveyor_module_2,
            camera=camera_module, 
            led_red=led_red, 
            led_green=led_green, 
            trapdoor_open=trapdoor_open, 
            trapdoor_close=trapdoor_close,
        )
        machine.setup()
        machine.led_green.on()
        machine.led_red.on()
        machine.init_sequence()
        
        # led_green.on()
        # led_red.on()
        
        atexit.register(machine.clear_all)
        # atexit.register(machine.turn_off)
        
        while True:
            machine.on_update()
            
    except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit()
            
    except Exception as e:
        print("failed to do something", e)
        GPIO.cleanup()
        sys.exit()