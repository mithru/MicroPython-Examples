# if button is pressed, it toggles the state of the LED and waits 300 milliseconds

while True:
	# Pin.value() gets the state of Pin and returns True of False
  if button_pin.value() == True:
    led.toggle()
    # adding a bit of a delay so the led doesn't toggle too fast
    pyb.delay(300)
