## setup ##
powered by Raspberry Pi Pico 2 W with RP2350 running MicroPython v1.25.0  
used:
- the two potentiometers:
   - B5K-50 to control the brightens
   - B5K-210 (with pins a t the bottom) to cntrol the speed of color rotation
- red, green, blue 5mm LEDS and acording resistors

  the rgb value at time t can be changed in func() at line 36
    I used sine-wawes, but it isnt the best solution to colour wawe for obvious reasons. (please give me a better solution)
