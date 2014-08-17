# USR button is controlled using a Switch object
# This is the one closer to the center of the pyboard
sw = pyb.Switch()
led = pyb.LED(4) # 4 is the blue LED

# toggles the LED when the USR button is released
# no need for while True: statement to keep this running
# read up on interrupts to understand how the below statement works
sw.callback(lambda:led.toggle())

'''
INTERRUPTS: 
to put it simply, when a function is registered with callback(), 
the microcontroller listens to a state change (low to high) on the USR button and registers this change. 
It then pauses any running code, executes the set function and resume code as usual
'''

'''
LAMBDA:
Python supports the creation of anonymous functions using lambda.
The above script could be rewritten to support user-defined functions as shown below.
Comment out the above script and uncomment the script below, and load it on your pyboard.
'''


'''
def toggleLED():
	pyb.LED(4).toggle()

sw.callback(toggleLED)
'''