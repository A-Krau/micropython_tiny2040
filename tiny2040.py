import machine
from machine import Pin
from machine import PWM
import scale

class Tiny2040:
    def __init__(self, freq=1000, duty = 65536):
        self.rgb_dict = {"red": 18, "grn": 19, "blu": 20}
        
        self.red = PWM(Pin(self.rgb_dict["red"]))
        self.grn = PWM(Pin(self.rgb_dict["grn"]))
        self.blu = PWM(Pin(self.rgb_dict["blu"]))

        self.red.freq(freq)
        self.grn.freq(freq)
        self.blu.freq(freq)
        
        self.red.duty_u16(duty)
        self.grn.duty_u16(duty)
        self.blu.duty_u16(duty)
        
    def color(self, r, g, b):
        self.rgb = {"red": r, "grn": g, "blu": b}
        self.red.duty_u16(self.rgb["red"])
        self.grn.duty_u16(self.rgb["grn"])
        self.blu.duty_u16(self.rgb["blu"])

    def blue_on(self):
        self.blu = {"red": 65536, "grn": 65536, "blu": 0}
        self.red.duty_u16(self.blu["red"])
        self.grn.duty_u16(self.blu["grn"])
        self.blu.duty_u16(self.blu["blu"])

    def red_on(self):
        self.red_dict = {"red": 0, "grn": 65536, "blu": 65536}
        self.red.duty_u16(self.red_dict["red"])
        self.grn.duty_u16(self.red_dict["grn"])
        self.blu.duty_u16(self.red_dict["blu"])

    def on(self):
        self.on_dict = {"red": 0, "grn": 0, "blu": 0}
        self.red.duty_u16(self.on_dict["red"])
        self.grn.duty_u16(self.on_dict["grn"])
        self.blu.duty_u16(self.on_dict["blu"])

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
