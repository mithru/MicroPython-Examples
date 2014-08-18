# USR button is controlled using a Switch object
# This is the one closer to the center of the pyboard
sw = pyb.Switch()
# connect an LED (with resistor) to pin X1 (the corner)
# a ground pin is two pins away.
pin = pyb.Pin('X1', pyb.Pin.OUT_PP) # configuring X1 to Push/Pull output

# LED is on only when the USR button is pressed down
while True:
	if sw() == True:
		pin.high()
	else:
		pin.low()
