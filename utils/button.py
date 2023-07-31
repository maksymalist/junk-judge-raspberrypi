import RPi.GPIO as GPIO

class Button:
    def __init__(self, pin) -> None:
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    def press_event(self, callback):
        GPIO.add_event_detect(self.pin, GPIO.RISING,callback=callback, bouncetime=500)