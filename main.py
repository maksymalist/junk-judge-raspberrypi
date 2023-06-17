from gpiozero import LED
import time

red_led = LED(17)

if __name__ == "__main__":
  while True:
    red_led.on()
    time.sleep(1)
    red_led.off()
    time.sleep(1)
