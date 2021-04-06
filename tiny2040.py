import machine
from machine import Pin
from machine import PWM
#import scale

class Tiny2040:
    def __init__(self, led_freq=1000, led_duty = 65536):
        self.rgb_dict = {"red": 18, "grn": 19, "blu": 20}
        self.led_freq = led_freq
        self.led_duty = led_duty
        
        self.red = PWM(Pin(self.rgb_dict["red"]))
        self.grn = PWM(Pin(self.rgb_dict["grn"]))
        self.blu = PWM(Pin(self.rgb_dict["blu"]))

        self.red.freq(led_freq)
        self.grn.freq(led_freq)
        self.blu.freq(led_freq)
        
        self.red.duty_u16(led_duty)
        self.grn.duty_u16(led_duty)
        self.blu.duty_u16(led_duty)
        
    def color(self, r, g, b):
        self.rgb = {"red": r, "grn": g, "blu": b}
        self.red.duty_u16(self.rgb["red"])
        self.grn.duty_u16(self.rgb["grn"])
        self.blu.duty_u16(self.rgb["blu"])

    def led_blue(self):
        self.blu = {"red": 65536, "grn": 65536, "blu": 0}
        self.red.duty_u16(self.blu["red"])
        self.grn.duty_u16(self.blu["grn"])
        self.blu.duty_u16(self.blu["blu"])

    def led_red(self):
        self.red_dict = {"red": 0, "grn": 65536, "blu": 65536}
        self.red.duty_u16(self.red_dict["red"])
        self.grn.duty_u16(self.red_dict["grn"])
        self.blu.duty_u16(self.red_dict["blu"])

    def on(self):
        self.on_dict = {"red": 0, "grn": 0, "blu": 0}
        self.red.duty_u16(self.on_dict["red"])
        self.grn.duty_u16(self.on_dict["grn"])
        self.blu.duty_u16(self.on_dict["blu"])
        
    def off(self):
        self.on_dict = {"red": 65536, "grn": 65536, "blu":65536}
        self.red.duty_u16(self.on_dict["red"])
        self.grn.duty_u16(self.on_dict["grn"])
        self.blu.duty_u16(self.on_dict["blu"])


