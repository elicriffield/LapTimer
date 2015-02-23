__author__ = 'elicriffield@gmail.com (Eli Criffield)'

import time

class LapTimer(object):
    car_times = {}
    car_laps = {}

    def __init__(self, minimum_lap=0):
        self.minimum_lap = minimum_lap

    def lap(self, car):
        now = time.time()
        if self.car_times.has_key(car):
            last = self.car_times[car]
            lap = now - last
            if lap < self.minimum_lap:
                return -1
            self._set_lap(car, lap)
            self.car_times[car] = now
            return lap
        else:
            self.car_times[car] = now
            return 0


    def _set_lap(self, car, time):
        if not self.car_laps.has_key(car):
            self.car_laps[car] = []
        self.car_laps[car].append(time)

    def get_car_laps(self, car):
        if not self.car_laps.has_key(car):
            return [0]
        return self.car_laps[car]

    def print_car_laps(self, car):
        if not self.car_laps.has_key(car):
            print 'Nothing found for {0:>s}'.format(car)
            return
        laps = 1
        print 'Laps for car {0}'.format(car)
        for lap_time in self.car_laps[car]:
            print 'Lap {0} : {1:.2f}'.format(laps, lap_time)
            laps += 1

    def reset_car(self, car):
        if self.car_laps.has_key(car):
            self.car_laps.pop(car)
        if self.car_times.has_key(car):
            self.car_times['car'] = time.time()
