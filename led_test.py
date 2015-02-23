#!/usr/bin/python
__author__ = 'elicriffield'

import rgb_led
import time
import sys

sleep = 0.01
longsleep = 1
rgb = rgb_led.RgbLed()


print "Red"
rgb.red()
time.sleep(longsleep)

print "Green"
rgb.green()
time.sleep(longsleep)

print "Blue"
rgb.blue()
time.sleep(longsleep)

print "Teal"
rgb.teal()
time.sleep(longsleep)

print "Purple"
rgb.purple()
time.sleep(longsleep)

print "Yellow"
rgb.yellow()
time.sleep(longsleep)

print "White"
rgb.white()
time.sleep(longsleep)

print "Off"
rgb.off()


print "Red ramp up then down"
for x in xrange(0,256):
    rgb.set_red_led(x)
    time.sleep(sleep)

for x in xrange(256,0,-1):
    rgb.set_red_led(x)
    time.sleep(sleep)

print "Green ramp up then down"
for x in xrange(0,256):
    rgb.set_green_led(x)
    time.sleep(sleep)

for x in xrange(256,0,-1):
    rgb.set_green_led(x)
    time.sleep(sleep)

print "Blue ramp up then down"
for x in xrange(0,256):
    rgb.set_blue_led(x)
    time.sleep(sleep)

for x in xrange(256,0,-1):
    rgb.set_blue_led(x)
    time.sleep(sleep)

rgb.off()

print "Green - Red"
for x in xrange(0,256):
    rgb.set_green_led(x)
    rgb.set_red_led(256-x)
    time.sleep(sleep*3)

rgb.off()

print "Green slow loop"
for x in xrange(0,257,64):
    print "Green {}".format(x)
    rgb.set_green_led(x)
    time.sleep(longsleep)

print "Off"
rgb.off()
