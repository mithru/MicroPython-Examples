import pyb

led = pyb.LED(4)
brightness = 0
fade_amount = 5

while True:
  led.intensity(brightness)
  brightness += fade_amount
  pyb.delay(30)

  if brightness >  255 or brightness < 0:
    fade_amount *= -1
