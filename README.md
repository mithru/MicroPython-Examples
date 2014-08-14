MicroPython-Examples
====================

This repo features examples for MicroPython similar to Arduino.

###00.Basics

__BareMinimum__  
A template that serves as a starting point

__HelloWorld__  
Turns on LED 4 (the blue LED).
An LED connected to pin 2 should work as well.

###01.LEDs

__Blink__ 
  
Replicates Arduino's Blink sketch exactly (uses .on() and .off())

Turns on LED 4 for 1000 milliseconds (1 second);  
Turns off LED 4 for 1000 milliseconds;  
loops  

__BlinkWithoutDelay__  
Replicates Arduino's BlinkWithoutDelay sketch (uses .toggle())

Same effect as Blink, but uses pyb.millis()

__BlinkWithToggle__  
Same as Blink, but uses .toggle()

__Fade__
Similar to Arduino's Fade sketch

Fades LED 4 on and off



