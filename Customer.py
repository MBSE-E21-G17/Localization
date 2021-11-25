import numpy as np

class Customer:
    def __init__(self, PATH,cust_id):
        self.PATH = PATH
        self.cur_pos = PATH[0]
        self.est_pos = [PATH[0]] #first estimation is at entrance
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
        if np.isfinite(pos[0]) and np.isfinite(pos[1]):
            self.est_pos += tmp #append to end of array
        else:
            self.est_pos.append(self.est_pos[self._time_index-1])

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
      
    
