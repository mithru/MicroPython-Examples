import pyb
# using ADC (analog digital converter)
pot_pin_adc = pyb.ADC(pyb.Pin.board.X1)

led = pyb.LED(4)


# led's intensity is controlled by the potentiometer's value

while True:
	# dividing by 16 since .read() gives a 12bit value
	# but .intensity() needs a 8bit value 
	# ensuring pot_value is an integer
	pot_value = int(pot_pin_adc.read()/16)
	led.intensity(pot_value)