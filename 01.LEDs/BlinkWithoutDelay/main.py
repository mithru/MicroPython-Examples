while True:
  curr_millis = pyb.millis()

  if curr_millis - prev_millis > interval:
    prev_millis = curr_millis

    led.toggle()
