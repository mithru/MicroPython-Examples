import pyb
import ultrasonic

# setting pins to accomodate Ultrasonic Sensor (HC-SR04)
sensor1_trigPin = pyb.Pin.board.X3
sensor1_echoPin = pyb.Pin.board.X4
sensor2_trigPin = pyb.Pin.board.Y3
sensor2_echoPin = pyb.Pin.board.Y4

# sensor needs 5V and ground to be connected to pyboard's ground

# creating two Ultrasonic Objects using the above pin config

sensor1 = ultrasonic.Ultrasonic(sensor1_trigPin, sensor1_echoPin)
sensor2 = ultrasonic.Ultrasonic(sensor2_trigPin, sensor2_echoPin)

# using USR switch to print the sensor's values when pressed

switch = pyb.Switch()

# function that prints each sensor's distance
def print_sensor_values():
	# get sensor1's distance in cm
	distance1 = sensor1.distance_in_cm()
	# get sensor2's distance in inches
	distance2 = sensor2.distance_in_inches()

	print("Sensor1 (Metric System)", distance1, "cm")
	print("Sensor2 (Imperial System)", distance2, "inches")

# prints values every second
while True:
	print_sensor_values()
	pyb.delay(1000)
