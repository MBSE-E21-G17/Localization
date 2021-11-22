import datetime
import random
import time


def timeNow():
    now = datetime.datetime.now()
    tid = now.strftime("%H:%M:%S:%f %p")
    return tid


class Customer:
    def __init__(self, PATH,cust_id):
        self.PATH = PATH
        self.cur_pos = PATH[0]
        #self.est_pos = (0, 0)
        self._path_ind = 0
        self.id = cust_id
        self.signal_cycle = 0
        self.signaling = 0

    def move(self):
        self.cur_pos = self.PATH[self._path_ind]
        self._path_ind =+ 1

    def update(self, Signal_rate, Signal_time):
        self.signal_cycle = (self.signal_cycle + 1) % Signal_rate

        if self.signal_cycle == 0 or self.signaling > 0:
            self.signaling = (self.signaling + 1) % Signal_time
        
        """
        for p in self.PATH:
            for a in p:
                self.cur_pos = a
                time.sleep(random.randrange(1, 10))
                print("Current position is : {}, at time {}".format(
                    self.cur_pos, timeNow()))
        """
    customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
