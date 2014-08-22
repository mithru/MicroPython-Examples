# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import pyb

'''
If your main function is not named 'main.py', 
the below line is required. 
Replace 'helloWorld.py' with the name of your 
script.
'''

pyb.main('helloWorld.py') # main script to run after this one



#pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
#pyb.usb_mode('CDC+HID') # act as a serial device and a mouse