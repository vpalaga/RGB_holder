from machine import ADC, Pin
import time
import math

adc_1 = ADC(26)  # rot Z
adc_2 = ADC(27)  # rot Y

G = Pin(5, Pin.OUT)
B = Pin(4, Pin.OUT)
R = Pin(3, Pin.OUT)

Pin(9, Pin.OUT).value(1)  # let 3,3 V into polynometer 2

hz = 200
t_add = .02



CON_F = 3.3 / 65535
MAX_V = 3.3
FPS = 1/hz
LED_OFF_TIME = FPS / 2
t = 0
a_B = 0

def get_speeds():
    raw_a = adc_1.read_u16() 
    raw_b = adc_2.read_u16()
    
    voltage_a = raw_a * CON_F
    voltage_b = raw_b * CON_F
    
    return voltage_a / MAX_V, voltage_b / MAX_V  # return float 0-1


def func(t):
    round(a_B, 2)
    r = math.sin(t) / 2 + 0.5  # fit into 0-1 range
    g = math.sin(t + math.pi * 2 / 3) / 2 + 0.5
    b = math.sin(t + math.pi *4 / 3) / 2 + 0.5
    
    return r * a_B, g * a_B, b * a_B
    #return 0, 0, 0 

def b_time(b):
    return (1 - b) * FPS
    

def light(t):
    
    r, g, b = func(t)
    
    off_times = [('R', b_time(r)), ('G', b_time(g)), ('B', b_time(b))]
    
    # Sort by the value (second item of each tuple)
    sorted_off_times = sorted(off_times, key=lambda x: x[1])

    # Now you can access both the sorted values and their original labels
    c_time = 0
    first = True
    for label, value in sorted_off_times:
        
            
        time.sleep(value - c_time)
        
        if (1 - value) >= LED_OFF_TIME:
            exec(f"{label}.value(1)")  # turn the led on

        c_time += value
        
    time.sleep(FPS - c_time)
    
    for l, v in off_times:
        exec(f"{l}.value(0)")  # reset rgbs to 0
        
    
while True:
    a, a_B = get_speeds()
    light(t)
    
    t += t_add * (a * 2)