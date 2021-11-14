import datetime
import random
import time


def timeNow():
    now = datetime.datetime.now()
    tid = now.strftime("%H:%M:%S:%f %p")
    return tid


class Customer:
    def __init__(self, PATH):
        self.PATH = PATH
        self.cur_pos = PATH[0]
        self.est_pos = (0, 0)
        self._path_ind = 0

    def move(self):
        for p in self.PATH:
            for a in p:
                self.cur_pos = a
                time.sleep(random.randrange(1, 10))
                print("Current position is : {}, at time {}".format(
                    self.cur_pos, timeNow()))

    customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
