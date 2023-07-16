import RPi.GPIO as GPIO
import time

class SMotorModule:
  def __init__(self, channels, wait_time) -> None:
    self.channels = channels
    self.wait_time = wait_time

  def setup(self):
    GPIO.setup(self.channels, GPIO.OUT) # setting the pins to output mode

  def rotate_clockwise(self, angle):

    for _ in range(angle):
      GPIO.output(self.channels, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
      time.sleep(self.wait_time)
      GPIO.output(self.channels, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
      time.sleep(self.wait_time)
      GPIO.output(self.channels, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
      time.sleep(self.wait_time)
      GPIO.output(self.channels, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
      time.sleep(self.wait_time)

  def rotate_counter_clockwise(self, angle):

    for _ in range(angle):
      GPIO.output(self.channels, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
      time.sleep(self.wait_time)
      GPIO.output(self.channels, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
      time.sleep(self.wait_time)
      GPIO.output(self.channels, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
      time.sleep(self.wait_time)
      GPIO.output(self.channels, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
      time.sleep(self.wait_time)
