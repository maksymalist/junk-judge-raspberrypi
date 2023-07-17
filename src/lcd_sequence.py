import RPi.GPIO as GPIO

def idle_mode(lcd, led_green):
    lcd.display("insert junk")
    GPIO.output(led_green, GPIO.HIGH)
    