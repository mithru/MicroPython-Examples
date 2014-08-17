MicroPython-Examples
====================

This repo features examples for MicroPython similar to Arduino.

###00.Basics

__BareMinimum__  
A template that serves as a starting point

__HelloWorld__  
Turns on LED 4 (the blue LED).

__REPL__  
REPL stands for Read-Eval-Print-Loop.  
Very important and highly useful feature that allows easy debugging and quick learning.  
All examples could be tested on the board without having to manually upload every time. 

__RunForever__  
A simple while True loop that mimicks Arduino's loop() at a very simple level

###01.LEDs

__Blink__  
Replicates Arduino's Blink sketch exactly (uses .on() and .off() and loops) 

__BlinkWithoutDelay__  
Replicates Arduino's BlinkWithoutDelay sketch (uses .toggle() and .millis())

__BlinkWithToggle__  
Same as Blink, but uses .toggle()

__Fade__  
Similar to Arduino's Fade sketch

__Heartbeat__  
Something more interesting that simple blinks 

__HeartbeatFade__  
Similar to previous 'Heartbeat' script, but fades the light in and out instead of just switching on and off  

###02.Inputs

__SimpleButton__  
Pull down button that toggles an LED

__Potentiometer__  
Simple analog input that controls an LED's intensity

__SwitchObject__  
Simple demo of the Switch object that can control the inbuilt USR button on the pyboard

__SwitchCallback__  
Example of the Switch.callback function (uses interrupts)

###03.Pins

_not yet updated - expect update by 19th Aug, 2014_

###04.Accelerometer

__AccelerometerControlLED__  
Controls blink speed of an LED using the accelerometer's value along the X axis  
This script also features a custom remap() function that remaps a value to different bounds/range  

__AccelerometerTest__  
Prints the x,y,z values of the accelerometer every second (REPL required)  

====================

Contributions include code from:  
[Mithru Vigneshwara](https://github.com/mithru/MicroPython-Examples/)  
[Dave Hylands](https://github.com/dhylands/upy-examples/)
