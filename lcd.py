#!/usr/bin/python

__author__ = 'elicriffield'


from ctypes import CDLL

class lcd(object):

    def __init__(self):
        self.lcd = CDLL("liblcd.so")

    def write_text(self, x, y, text):
        self.lcd.write_text(x, y, text)

    def clear(self):
        self.lcd.clear()

    def contrast(self,c):
        self.lcd.contrast(c)

    def backlight(self,b):
        self.lcd.backlight(b)
