import machine
from machine import Pin
from machine import PWM
#import scale

class Tiny2040:
    def __init__(self, led_freq=1000, led_duty = 65536):
        """Set up Tiny2040 class.
        
        led_freq will default to 1000 if not passed in argument.
        led_duty will default to 65536 if not passed in argument.
        
        When initialized led will be off.
        """
        self.rgb_dict = {"red": 18, "grn": 19, "blu": 20} 
        self.led_freq = led_freq
        self.led_duty = led_duty
        
        #set up all pins associated with RBB led.
        self.red = PWM(Pin(self.rgb_dict["red"]))
        self.grn = PWM(Pin(self.rgb_dict["grn"]))
        self.blu = PWM(Pin(self.rgb_dict["blu"]))

        #set all all channels to passed led_freq
        self.red.freq(led_freq)
        self.grn.freq(led_freq)
        self.blu.freq(led_freq)
        
        #set all channels to passed led_duty
        self.red.duty_u16(led_duty)
        self.grn.duty_u16(led_duty)
        self.blu.duty_u16(led_duty)
        
    def color(self, r, g, b):
        """Pass values as r, g, b values from 0 - 65536
        0 is full on
        65536 is full off
        """
        self.rgb = {"red": r, "grn": g, "blu": b}
        self.red.duty_u16(self.rgb["red"])
        self.grn.duty_u16(self.rgb["grn"])
        self.blu.duty_u16(self.rgb["blu"])

    def led_blue(self):
        """Set led to blue"""
        self.blu_dict = {"red": 65536, "grn": 65536, "blu": 0}
        self.red.duty_u16(self.blu_dict["red"])
        self.grn.duty_u16(self.blu_dict["grn"])
        self.blu.duty_u16(self.blu_dict["blu"])

    def led_red(self):
        """Set led to red"""
        self.red_dict = {"red": 0, "grn": 65536, "blu": 65536}
        self.red.duty_u16(self.red_dict["red"])
        self.grn.duty_u16(self.red_dict["grn"])
        self.blu.duty_u16(self.red_dict["blu"])

    def led_green(self):
        """Set led to green"""
        self.green_dict = {"red": 0, "grn": 65536, "blu": 65536}
        self.red.duty_u16(self.green_dict["red"])
        self.grn.duty_u16(self.green_dict["grn"])
        self.blu.duty_u16(self.green_dict["blu"])
        
    def on(self):
        """Set led to white"""
        self.on_dict = {"red": 0, "grn": 0, "blu": 0}
        self.red.duty_u16(self.on_dict["red"])
        self.grn.duty_u16(self.on_dict["grn"])
        self.blu.duty_u16(self.on_dict["blu"])
        
    def off(self):
        """Set led to off"""
        self.on_dict = {"red": 65536, "grn": 65536, "blu":65536}
        self.red.duty_u16(self.on_dict["red"])
        self.grn.duty_u16(self.on_dict["grn"])
        self.blu.duty_u16(self.on_dict["blu"])
