__author__ = 'eli'

import lcd

class Display(object):

  def __init__(self):
    self.lcd = lcd.lcd()
    self.lcd.clear()
    self.where_to_write = 1

  def clear(self):
    self.lcd.clear()

  def r1p1(self, car, time):
    to_display = '{0}:{1:05.2f}  '.format(car[:1],time)
    self.lcd.write_text(0,0,to_display)

  def r1p2(self, car, time):
    to_display = '{0}:{1:05.2f}'.format(car[:1],time)
    self.lcd.write_text(9,0,to_display)

  def r2p1(self, car, time):
    to_display = '{0}:{1:05.2f}  '.format(car[:1],time)
    self.lcd.write_text(0,1,to_display)

  def r2p2(self, car, time):
    to_display = '{0}:{1:05.2f}'.format(car[:1],time)
    self.lcd.write_text(9,1,to_display)

  def next(self, car, time):
    if self.where_to_write == 1:
      self.r1p1(car, time)
    elif self.where_to_write == 2:
      self.r1p2(car, time)
    elif self.where_to_write == 3:
      self.r2p1(car, time)
    elif self.where_to_write == 4:
      self.r2p2(car, time)
    self.where_to_write += 1
    if self.where_to_write == 5:
      self.where_to_write = 1