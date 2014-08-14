import pyb

led = pyb.LED(4)
while True:
  led.on()
  delay(1000)
  led.off()
  delay(1000)
