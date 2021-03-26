import time
import machine
from machine import Pin
from machine import PWM

class Tiny2040:
    def __init__(self, freq, duty):
        self.rgb_dict = {"red": 18, "grn": 19, "blu": 20}
        if freq is None:
            self.freq = 1000 
        else:
            self.freq = freq
        if duty is None:
            self.duty = 65532
        else:
            self.duty = duty
        for key in self.rgb_dict:
            self.key = PWM(Pin(self.rgb_dict[key]))
            print("worked to here")
            self.key.freq(self.freq)
            self.key.duty_u16(self.duty)
            
    def color(self, r, g, b):
        rgb = {"red": r, "grn": g, "blu": b}
        for key in self.rgb_dict:
            print(key+ "_: " + str(rgb[key]))
            self.key.duty_u16(rgb[key])
        