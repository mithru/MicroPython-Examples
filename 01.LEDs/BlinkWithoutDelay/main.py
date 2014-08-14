import pyb

led = pyb.LED(4)
prev_millis = 0
interval = 1000

while True:
  curr_millis = pyb.millis()

  if curr_millis - prev_millis > interval:
    prev_millis = curr_millis

    led.toggle()
