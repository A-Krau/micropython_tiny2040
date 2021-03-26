from machine import Pin
from machine import PWM
import time


rgb_dict = {"red": 18, "grn": 19, "blu": 20}
rgb = {"red": 65532, "grn": 65535, "blu": 65535}

freq = 1000 
duty = 0


for key in rgb_dict:
    print(key)
    print(rgb_dict[key])
    key = PWM(Pin(rgb_dict[key]))
    key.freq(freq)
    key.duty_u16(duty)

time.sleep(1)
blu.duty_u16(65532)

#for key in rgb_dict:
#    print(key + "_: " + str(rgb[key]))
#    key.duty_u16(rgb[key])
