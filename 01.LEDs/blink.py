import pyb

# The pyboard has 4 LEDs that can be controlled
# these LEDs have IDs 1 - 4

led = pyb.LED(4)  # 4 is the blue LED

# toggle LED state every second using on() and off() methods
while True:
  led.on()
  pyb.delay(1000)
  led.off()
  pyb.delay(1000)
