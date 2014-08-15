# potentiometer is connected to X1

import pyb
# using ADC (analog digital converter)
pot_pin_adc = pyb.ADC(pyb.Pin.board.X1)

led = pyb.LED(4)
