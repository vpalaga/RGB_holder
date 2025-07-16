## setup ##
powered by Raspberry Pi Pico 2 W with RP2350 running MicroPython v1.25.0  
## 3D model ##   
[stone holder]( https://cad.onshape.com/documents/12652b33271f7d0f3e3c2148/w/75f9bf42905b6c702b97d5b1/e/94e5234fc7dac11d9bea0b94?renderMode=0&uiState=68782b38c07ba16fa4912e08 )   
---
used:
- the two potentiometers:
   - B5K-50 to control the brightens
   - B5K-210 (with pins a t the bottom) to cntrol the speed of color rotation
- red, green, blue 5mm LEDS and acording resistors

  the rgb value at time t can be changed in func() at line 36
    I used sine-wawes, but it isnt the best solution to colour wawe for obvious reasons. (please give me a better solution)
