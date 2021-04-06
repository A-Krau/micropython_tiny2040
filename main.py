from tiny2040 import Tiny2040
from time import sleep

led = Tiny2040()

led.off()

while True:
    led.on()
    sleep(1)
    led.led_r()
    sleep(1)
    led.led_g()
    sleep(1)
    led.led_b()
    sleep(1)
