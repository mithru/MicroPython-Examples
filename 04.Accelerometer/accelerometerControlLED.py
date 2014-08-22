import pyb

led = pyb.LED(3)

acc = pyb.Accel()

# the below function can be used to remap values
# syntax: remap(input_value, input_lowerbount, input_upperbound, output_lowerbound, output_upperbound) returns output_value 
def remap(i_val, i_start, i_stop, o_start, o_stop):
	o_val =  o_start + (o_stop - o_start) * ((i_val - i_start)/(i_stop - i_start))
	return o_val
	

while True:
	# remap values from accelerometer to be within range 10-1000
	# the micropython docs suggest that the accelerometer maintains a range roughly between -30 and 30
	intensity = int(remap(acc.x(), -30, 30, 10, 1000))
	led.toggle()
	pyb.delay(intensity)