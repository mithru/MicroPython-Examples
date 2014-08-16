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


====================

Contributions include code from:  
[Mithru Vigneshwara](https://github.com/mithru/MicroPython-Examples/)  
[Dave Hylands](https://github.com/dhylands/upy-examples/)
