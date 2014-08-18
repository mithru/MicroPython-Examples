servo = pyb.Servo(1) # id can be 1-4 (corresponds to pins X1 - X4)

while True:
  
  #set servo's position immediately
  servo.angle(90) # in degrees
  # many common servos have a range between -90 and 90 degrees
  
  pyb.delay(500) # wait half a second
  
  # change servo position to specified angle 
  # and take a specified time to reach that angle
  servo.angle(-90, 2000) # 2000 millis = 2 seconds
  
  pyb.delay(3000) # delaying by 3 seconds since it'll take two seconds for the motor to reach its final state
  
  # the above statement makes the motor spin to -90 and then move on.
  # if your motors range does not hold -90, it could stall at this point
  # run servo.angle() to get your motor's position 
  

