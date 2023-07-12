import drivers
import time
import sys


class LcdModule:
  def __init__(self, lcd) -> None:
    self.screen = lcd

  def display(self, message):
    self.screen.lcd_display_string(message, 1)

