# from utils.firebase import upload_file_to_firebase
# from utils.notion import create_notion_entry
# from utils.model import predict_type
from picamera import PiCamera
from utils.lcd_display import LcdModule
from utils.stepper_motor import SMotorModule
from utils.camera import CameraModule
from src.machine import JunkJudge

import drivers
import RPi.GPIO as GPIO

if __name__ == "__main__":

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    
    camera = PiCamera()
    screen = drivers.Lcd()
    
    camera_module = CameraModule(camera, (500, 500), 50)
    lcd_module = LcdModule(screen)
    stepper_motor_module = SMotorModule((29,31,33,35), 0.002)
    
    led_red = 38
    led_green = 40 
    
    
    machine = JunkJudge(lcd_module, stepper_motor_module, camera_module, led_red, led_green)
    
    machine.init()





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
    
