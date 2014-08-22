import pyb

servo = pyb.Servo(1) # id can be 1-4 (corresponds to pins X1 - X4)

while True:
  # generates a random 30-bit number
  # dividing so we get a smaller number to work with roughly 0 - 200
  random_angle = pyb.rng() // 5500000
  
  # subtracting by 90 to bring range to roughly between -90 and 90
  # since many common servos have a range between -90 and 90 degrees
  random_angle -= 90 
  
  #set servo's position immediately to random_angle
  servo.angle(random_angle) # in degrees
  
  pyb.delay(500) # wait half a second
  
  print(servo.angle()) # prints the servo's current position
  
  pyb.delay(500)