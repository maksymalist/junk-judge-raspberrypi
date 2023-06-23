import drivers
import time
import sys


class LcdModule:
  def __init__(self, lcd, string) -> None:
    self.screen = lcd
    self.string = string

  def display(self):
    self.screen.lcd_display_string(self.string, 1)

