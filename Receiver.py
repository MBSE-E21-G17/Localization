import numpy as np
import random


class Receiver:
    def __init__(self, Signal_radius):
        self.Data_result = []  # hold received signals
        self.Pos = [0, 0]  # Position of receiver in world
        self._Signal_radius = Signal_radius  # How far the signal can be received
        self._time_index = 0  # Index for data array logic

    def append_signal(self, cust_id, cust_pos):
        """
        This function addes the recived signals to the data array of the
        reciver
            cust_id = id of signal from customer, i.e. customer 1 has id 1
            cust_pos = position of customer when sending signal
        """

        tmp = [(cust_id, self._distance(cust_pos))]  # The signal id
        if len(self.Data_result) == 0:  # if first signal to be recived
            self.Data_result += tmp

        # Add signal to array if signal in signal radius
        elif self._distance(cust_pos) <= self._Signal_radius:
            if len(self.Data_result) == self._time_index:
                self.Data_result += tmp
            else:
                # print("OVERLAP IN SIGNAL")
                self.Data_result[self._time_index] = 0

    def __str__(self):
        return str(self.Pos)

    def __repr__(self):
        return self.__str__()

    def clear_signal(self, signal_rate):
        print(self.Data_result)
        for i in range(len(self.Data_result)):
            if type(self.Data_result[i]) is tuple:
                print(i)
                print("len: " + str(self._time_index))
                cust_id = self.Data_result[i][0]
                for k in range(0, signal_rate - 1):
                    print("k: " + str(k))
                    if k + i > self._time_index - 1:
                        print("Break")
                        break

                    if self.Data_result[i + k][0] != cust_id:
                        self.Data_result[i + k] = 0
        print(self.Data_result)

    def _distance(self, cust_pos):
        """
        This function calculates the distance the signal propigates 
        using pythagoran formula
        """
        return np.sqrt((cust_pos[0] - self.Pos[0]) ** 2 + (cust_pos[1] - self.Pos[1]) ** 2)

    def update(self):
        """ 
        This function updates the time index of the reciver.
        Needs to be called at the end of  every time interval
        """
        if self._time_index < len(self.Data_result):
            self._time_index += 1
        else:
            self.Data_result.append(0)
            self._time_index += 1
