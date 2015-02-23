#!/usr/bin/python

__author__ = 'elicriffield@gmail.com (Eli Criffield)'

import pylirc
import timer
import time
from timer_lcd import Display
from rgb_led import RgbLed
from datetime import datetime
import sys
import traceback
import IPython
import subprocess


def execpt(*args, **kwargs):
  now = datetime.now()
  error_log = '/home/pi/log/ir_timer_error.{0}{1}{2}{3}{4}'.format(
    now.year, now.month, now.day, now.hour, now.minute)
  fd = open(error_log, 'w')
  traceback.print_exception(*args,file=fd)
  traceback.print_exception(*args)
  fd.close()
  led.white()


sys.excepthook = execpt

t = timer.LapTimer(minimum_lap=5)
lcd = Display()
time.sleep(1)
lcd.lcd.clear()
ip = subprocess.check_output(['/bin/hostname','-I']).strip()
lcd.lcd.write_text(0,0,ip)
led = RgbLed(pwm=False)
led.teal()
print "Ready"

blocking = 1
if pylirc.init("pylirc", "/etc/lirc/lircrc", blocking):
   now = datetime.now()
   log = '/home/pi/log/ir_timer_log.{0}{1}{2}{3}{4}'.format(
       now.year, now.month, now.day, now.hour, now.minute)
   code = {"config" : ""}
   while(code["config"] != "quit"):

      # Read next code
      s = pylirc.nextcode(1)

      # Loop as long as there are more on the queue
      # (dont want to wait a second if the user pressed many buttons...)
      while(s):
         
         # Print all the configs...
         for (code) in s:
            car = code["config"]
            led.red()
            print "Car: %s, Repeat: %d" % (car, code["repeat"])
            lap = t.lap(car)
            if lap != -1:
              lcd.next(car, lap)
              if lap:
                led.green()
                print '{0}:{1:5.2f}'.format(car, lap)
                open(log,'a').write('{0}:{1:5.2f}\n'.format(car, lap))
              else:
                led.purple()
                print 'First Lap for {0}'.format(car)
                open(log,'a').write('First Lap for {0}\n'.format(car))

            time.sleep(0.5)
            led.off()
            blocking = 1
            pylirc.blocking(1)

         s = []

   # Clean up lirc
   pylirc.exit()
