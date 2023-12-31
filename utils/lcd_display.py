import drivers
import time
import sys


class LcdModule:
  def __init__(self, lcd) -> None:
    self.screen = lcd
    
  def setup_custom_characters(self):
    
    # Create object with custom characters data
    cc = drivers.CustomCharacters(self.screen)

    # Redefine the default characters that will be used to create process bar:
    # Left full character. Code {0x00}.
    cc.char_1_data = ["01111",
                      "11000",
                      "10011",
                      "10111",
                      "10111",
                      "10011",
                      "11000",
                      "01111"]

    # Left empty character. Code {0x01}.
    cc.char_2_data = ["01111",
                      "11000",
                      "10000",
                      "10000",
                      "10000",
                      "10000",
                      "11000",
                      "01111"]

    # Central full character. Code {0x02}.
    cc.char_3_data = ["11111",
                      "00000",
                      "11011",
                      "11011",
                      "11011",
                      "11011",
                      "00000",
                      "11111"]

    # Central empty character. Code {0x03}.
    cc.char_4_data = ["11111",
                      "00000",
                      "00000",
                      "00000",
                      "00000",
                      "00000",
                      "00000",
                      "11111"]

    # Right full character. Code {0x04}.
    cc.char_5_data = ["11110",
                      "00011",
                      "11001",
                      "11101",
                      "11101",
                      "11001",
                      "00011",
                      "11110"]

    # Right empty character. Code {0x05}.
    cc.char_6_data = ["11110",
                      "00011",
                      "00001",
                      "00001",
                      "00001",
                      "00001",
                      "00011",
                      "11110"]

    # Load custom characters data to CG RAM:
    cc.load_custom_characters_data()

  def display(self, message, line=1):
    self.screen.lcd_display_string(message, line)
    
  def display_progress(self, progress, message):

    bar_repr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Remember that your sentences can only be 16 characters long!
    self.screen.lcd_display_string("", 1)
    
        
    # Render charge bar:
    bar_string = ""
    
    for i in range(10):
        if progress >= ((i + 1) * 10):
            bar_repr[i] = 1
        else: 
            bar_repr[i] = 0  
    
    for i in range(10):
      if i == 0:
          # Left character
          if bar_repr[i] == 0:
              # Left empty character
              bar_string = bar_string + "{0x01}"
          else:
              # Left full character 
              bar_string = bar_string + "{0x00}"
      elif i == 9:
          # Right character
          if bar_repr[i] == 0:
              # Right empty character
              bar_string = bar_string + "{0x05}"
          else:
              # Right full character
              bar_string = bar_string + "{0x04}"
      else:
          # Central character
          if bar_repr[i] == 0:
              # Central empty character
              bar_string = bar_string + "{0x03}"
          else:
              # Central full character
              bar_string = bar_string + "{0x02}"
                
      # Print the string to display:
    self.screen.lcd_display_string("                ", 1)
    self.screen.lcd_display_string(message, 1)
    self.screen.lcd_display_extended_string(bar_string + " {0}% ".format(progress), 2)     

    
  def clear(self):
    self.screen.lcd_clear()

