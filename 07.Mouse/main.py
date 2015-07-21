# main.py -- put your code here!
import pyb

switch = pyb.Switch()
accel = pyb.Accel()

while True:
	pyb.hid((switch(), accel.x(), -accel.y(), 0))
	pyb.delay(20)
