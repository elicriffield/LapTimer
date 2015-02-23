__author__ = 'elicriffield'

import wiringpi
import time
import sys

class RgbLed(object):
    MIN = 0
    MAX = 256

    red_led_value = MIN
    green_led_value = MIN
    blue_led_value = MIN


    def __init__(self, red=7, green=1, blue=8, invert=True, pwm=True):
        wiringpi.wiringPiSetup()

        self.red_led = red
        self.green_led = green
        self.blue_led = blue
        self.invert = invert
        self.pwm = pwm

        for led in (red, green, blue):
            if pwm:
                if led is 1:
                    # pin 1 has hardware PWM
                    wiringpi.pinMode(led, wiringpi.PWM_OUTPUT)
                    self.pin1_multiplier = 1024 / self.MAX
                else:
                    wiringpi.softPwmCreate(led, self.MIN, self.MAX)
            else:
                wiringpi.pinMode(led, wiringpi.OUTPUT)

        self.set_red_led(self.red_led_value)
        self.set_green_led(self.green_led_value)
        self.set_blue_led(self.blue_led_value)

    def led_write(self, led, value):
        if self.invert:
            value = self.MAX - value
        if self.pwm:
            if led is 1:
                wiringpi.pwmWrite(led, (value * self.pin1_multiplier))
            else:
                wiringpi.softPwmWrite(led, value)
        else:
            wiringpi.digitalWrite(led, value)

    def set_red_led(self, value):
        self.red_led_value = value
        self.led_write(self.red_led, value)

    def set_green_led(self, value):
        self.green_led_value = value
        self.led_write(self.green_led, value)

    def set_blue_led(self, value):
        self.blue_led_value = value
        self.led_write(self.blue_led, value)


    def set_rgb(self, red, green, blue):
        self.set_red_led(red)
        self.set_green_led(green)
        self.set_blue_led(blue)

    def red(self):
        self.set_rgb(red=self.MAX,green=self.MIN,blue=self.MIN)

    def green(self):
        self.set_rgb(red=self.MIN,green=self.MAX,blue=self.MIN)

    def blue(self):
        self.set_rgb(red=self.MIN,green=self.MIN,blue=self.MAX)

    def purple(self):
        self.set_rgb(red=self.MAX,green=self.MIN,blue=self.MAX)

    def yellow(self):
      self.set_rgb(red=self.MAX,green=self.MAX,blue=self.MIN)

    def teal(self):
        self.set_rgb(red=self.MIN,green=self.MAX,blue=self.MAX)

    def white(self):
        self.set_rgb(red=self.MAX,green=self.MAX,blue=self.MAX)

    def off(self):
        self.set_rgb(red=self.MIN,green=self.MIN,blue=self.MIN)


