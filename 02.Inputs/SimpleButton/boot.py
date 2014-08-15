# A push button is connected with a pull down resistor to pin X1

# X1 is the pin at the bottom-left corner of the board 
# (USB port pointing right, ARM chip facing the user)

import pyb

# set variable button_pin to Pin 'X1' 
button_pin = pyb.Pin('X1', pyb.Pin.IN)
led = pyb.LED(4)
