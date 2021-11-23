import datetime
import random
import time


def timeNow():
    now = datetime.datetime.now()
    tid = now.strftime("%H:%M:%S:%f %p")
    return tid


class Customer:
    def __init__(self, PATH,cust_id):
        self.PATH = PATH[0]
        self.cur_pos = PATH[0][0]
        self.est_pos = [(0,0)]
        self._path_ind = 0
        self.id = cust_id
        self.signal_cycle = 0
        self.signaling = 0
        self.END = False
        self._time_index = 0  # Practicaly the same as path_ind
        self.left = False

    def move(self):
        if len(self.PATH) != self._path_ind:
            self.cur_pos = self.PATH[self._path_ind]
            self._path_ind += 1
        else:
            self.END = True

    def append_est_pos(self,pos):
        tmp = [pos]
        self.est_pos += tmp #append to end of array

    def update(self, Signal_rate, Signal_time):
        if not self.END:
            self.signal_cycle = (self.signal_cycle + 1) % Signal_rate

            if self.is_signaling():
                self.signaling = (self.signaling + 1) % Signal_time

            if self._time_index < len(self.est_pos):
                self._time_index += 1
            else: # Estemated position has not been calculated
                self.est_pos.append(self.est_pos[self._time_index-1])
                self._time_index += 1


    def is_signaling(self):
        return (self.signal_cycle == 0 or self.signaling > 0) and not self.END
        """
        for p in self.PATH:
            for a in p:
                self.cur_pos = a
                time.sleep(random.randrange(1, 10))
                print("Current position is : {}, at time {}".format(
                    self.cur_pos, timeNow()))
        """
    customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
