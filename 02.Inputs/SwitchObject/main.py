# USR button is controlled using a Switch object
# This is the one closer to the center of the pyboard
sw = pyb.Switch()
led = pyb.LED(4) # 4 is the blue LED

# LED is on only when the USR button is pressed down
while True:
	if sw() == True:
		led.on()
	else:
		led.off()
