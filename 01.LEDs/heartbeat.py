import pyb
led = pyb.LED(4)

tick = 0 # counter variable

while True:
	if tick <= 3:
		led.toggle()
	#make sure the value of tick has a 0-9 range
	tick = (tick + 1) % 10
	pyb.delay(100)