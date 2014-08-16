# simplest way to loop forever:
while True:
  led.on()
  pyb.delay(10)
  led.off()
  pyb.delay(10)
