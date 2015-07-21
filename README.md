MicroPython-Examples
====================

This repo features examples for MicroPython similar to Arduino.

###00.Basics

__boot.py__  
Sample boot file which points to 'helloWorld.py' to run after booting. The examples in this repo will not include copies of the boot file. Please edit and include boot.py accordingly. 

__helloWorld.py__  
Turns on LED 4 (the blue LED).

__REPL__  
REPL stands for Read-Eval-Print-Loop.  
Very important and highly useful feature that allows easy debugging and quick learning.  
All examples can be tested on the board without having to manually upload every time. 

====================
  
###01.LEDs

__blink__  
Replicates Arduino's Blink sketch exactly (uses .on() and .off() and loops) 

__blinkWithoutDelay__  
Replicates Arduino's BlinkWithoutDelay sketch (uses .toggle() and .millis())

__blinkToggle__  
Same as Blink, but uses .toggle()

__fade__  
Similar to Arduino's Fade sketch

__heartbeat__  
Something more interesting that simple blinks 

__heartbeatFade__  
Similar to previous 'Heartbeat' script, but fades the light in and out instead of just switching on and off  

====================

###02.Inputs

__button__  
Pull down button that toggles an LED

__potentiometer__  
Simple analog input that controls an LED's intensity

__switchObject__  
Simple demo of the Switch object that can control the inbuilt USR button on the pyboard

__switchCallback__  
Example of the Switch.callback function (uses interrupts)

====================

###03.Pins

__PinsBasicOutput__  
Example of using on of the pins to control an output (LED, motor, buzzer, relay, et al)

====================

###04.Accelerometer

__accelerometerControlLED__  
Controls blink speed of an LED using the accelerometer's value along the X axis  
This script also features a custom remap() function that remaps a value to different bounds/range  

__accelerometer__  
Prints the x,y,z values of the accelerometer every second (REPL required)  

====================

###05.Servos

__ServoSetAngle__  
Example of setting a servo's angle, and animating it over time

__ServoGetAngle__  
Generates a random number roughly between -90 and 90, and sets it as the servo's angle. The servo's angle is then obtained from the object

====================

###06.Clock

__clock__  
Uses the RTC (independent Real Time Clock) in the pyboard. Prints the time and date with delay of 100 microseconds. Start time is set with variables.

====================

Contributions include code from:  
[Mithru Vigneshwara](https://github.com/mithru/MicroPython-Examples/)  
[Dave Hylands](https://github.com/dhylands/upy-examples/)
