# A push button is connected with a pull down resistor to pin X1

# X1 is the pin at the bottom-left corner of the board 
# (USB port pointing right, ARM chip facing the user)

import pyb

# set variable button_pin to Pin 'X1' 
button_pin = pyb.Pin('X1', pyb.Pin.IN)
led = pyb.LED(4)

# if button is pressed, it toggles the state of the LED and waits 300 milliseconds

while True:
	# Pin.value() gets the state of Pin and returns True of False
  if button_pin.value() == True:
    led.toggle()
    # adding a bit of a delay so the led doesn't toggle too fast
    pyb.delay(300)
