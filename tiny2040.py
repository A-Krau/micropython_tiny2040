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
        self.red = PWM(Pin(self.rgb_dict["red"]))
        self.grn = PWM(Pin(self.rgb_dict["grn"]))
        self.blu = PWM(Pin(self.rgb_dict["blu"]))

        self.red.freq(self.freq)
        self.grn.freq(self.freq)
        self.blu.freq(self.freq)
        
        self.red.duty_u16(self.duty)
        self.grn.duty_u16(self.duty)
        self.blu.duty_u16(self.duty)
        
    def color(self, r, g, b):
        self.rgb = {"red": r, "grn": g, "blu": b}
        self.red.duty_u16(self.rgb["red"])
        self.grn.duty_u16(self.rgb["grn"])
        self.blu.duty_u16(self.rgb["blu"])
