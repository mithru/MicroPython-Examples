# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import pyb

'''
If your main function is not named 'main.py', 
the below line is required. 
Replace 'helloWorld.py' with the name of your 
script.
'''

'''
If you're using the MicroPython-Examples github repo,
just uncomment the required line.
'''

#00.Basics/

pyb.main('helloWorld.py') # main script to run after this one


#01.LEDs/

#pyb.main('blink.py') 
#pyb.main('blinkToggle.py') 
#pyb.main('blinkWithoutDelay.py') 
#pyb.main('fade.py') 
#pyb.main('heartbeat.py') 
#pyb.main('heartbeatFade.py') 


#02.Inputs/

#pyb.main('button.py') 
#pyb.main('potentiometer.py') 
#pyb.main('switch.py') 
#pyb.main('switchCallback.py') 


#03.Pins/

#pyb.main('PinsBasicOutput.py') 


#04.Accelerometer/

#pyb.main('accelerometer.py') 
#pyb.main('accelerometerControlLED.py') 


#05.Servos

#pyb.main('ServoGetAngle.py') 
#pyb.main('ServoSetAngle.py')


#06.Clock

#pyb.main('clock.py') 


#07.Mouse
# has it's own boot.py (this needs to be placed better)

#08.Sensors

#pyb.main('HC-SR04.py') 


#pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
#pyb.usb_mode('CDC+HID') # act as a serial device and a mouse
