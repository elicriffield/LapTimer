#!/usr/bin/python
__author__ = 'elicriffield'

import rgb_led
import sys

color = sys.argv[1]
led = rgb_led.RgbLed(pwm=False)

if color == 'red':
    led.red()
elif color == 'green':
    led.green()
elif color == 'blue':
    led.blue()
elif color == 'purple':
    led.purple()
elif color == 'yellow':
    led.yellow()
elif color == 'white':
    led.white()
elif color == 'off':
    led.off()
