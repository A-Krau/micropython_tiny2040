from machine import Pin
from machine import PWM
import time
from tiny2040 import Tiny2040

led = Tiny2040(None,None)


while True:
    led.color(0, 65532, 0)
    time.sleep(1)
    led.color(0, 0, 0)
    time.sleep(1)