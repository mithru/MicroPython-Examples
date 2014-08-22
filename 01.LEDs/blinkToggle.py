import pyb

led = pyb.LED(2)

while True:
  led.toggle()
  pyb.delay(1000)
