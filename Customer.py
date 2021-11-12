import datetime
import random
import time


class Customer:
    def __init__(self, PATH):
        self.PATH = PATH
        self.cur_pos = PATH[0]
        self.est_pos = (0, 0)
        self._path_ind = 0

    def move(self):
        # if len(self.PATH) + 1 == self._path_ind:
        #     return
        for p in self.PATH:
            for a in p:
                now = datetime.datetime.now()
                datetime1 = now.strftime("%H:%M:%S:%f %p")

                self.cur_pos = a
                time.sleep(random.randrange(1, 10))
                print("Current position is : {}, at time {}".format(
                    self.cur_pos, datetime1))

    customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
