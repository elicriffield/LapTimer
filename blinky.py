#!/usr/bin/python

__author__ = 'elicriffield'

import atexit
import rgb_led
from time import sleep

led = rgb_led.RgbLed(pwm=False)
atexit.register(led.off)

sleep_time = 0.5
while True:
    led.red()
    sleep(sleep_time)
    led.green()
    sleep(sleep_time)
    led.blue()
    sleep(sleep_time)
    led.purple()
    sleep(sleep_time)
    led.teal()
    sleep(sleep_time)
    led.yellow()
    sleep(sleep_time)
    led.white()
    sleep(sleep_time)
    
    