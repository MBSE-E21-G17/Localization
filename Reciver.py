import numpy as np
import random as rand

class Reciver:
    def __init__(self,pos_x,pos_y, Signal_radius):
        self.Data_result = []
        self.Pos = (pos_x,pos_y)
        self._Signal_radius = Signal_radius
        self._time_index = 0

    def append_signal(self, cust_id, cust_pos, ts,curr_time):
        print(self._time_index)
        print(curr_time)
        print(self.Data_result)
        tmp = [cust_id]
        if self._distance(cust_pos) <= self._Signal_radius and self.Data_result[self._time_index-1] == 0:
            self.Data_result += tmp 
            


    def clear_signal(self, ts_1, ts_2):
        pass

    def _distance(self, cust_pos):
        return np.sqrt((cust_pos[0] - self.Pos[0])**2 + (cust_pos[1] - self.Pos[1])**2)
    
    def update(self):
        if self._time_index <= len(self.Data_result):
            self._time_index += 1
        else:
            self.Data_result.append(0)
            self._time_index += 1

def Update_recivers(Recivers):
    for i in  range(len(Recivers)):
        Recivers[i].update()

def Init_Recivers(N,ts):
    Recivers = [0]*N
    for i in range(0,N):
        Recivers[i] = Reciver(rand.randrange(0,5),rand.randrange(0,5),ts)
    return Recivers


if __name__ == "__main__":
    
    rand.seed(2)
    N = 3
    SIGNAL_RATE = 8
    SIGNAL_TIME = 3
    SIGNAL_STRENGHT = 100


    Recivers = Init_Recivers(N,SIGNAL_STRENGHT)
    print(Recivers[0].Pos)
    print(Recivers[1].Pos)
    cust1_signal_rate = 0
    cust1_signaling = 0

    cust2_signal_rate = 2
    cust2_signaling = 0
    
    for i in range(0,20):
        
        Update_recivers(Recivers)
        print(i)
        if cust1_signal_rate == 0 or cust1_signaling > 0:
            print("CUST 1 SIGNALING")
            Recivers[0].append_signal(1,(2,3),SIGNAL_TIME,i)
            cust1_signaling = (cust1_signaling + 1) % SIGNAL_TIME
        """
        if cust2_signal_rate == 0 or cust1_signaling > 0:
            print("CUST 2 SIGNALING")
            Recivers[0].append_signal(2,(2,3),SIGNAL_TIME,i)
            cust2_signaling = (cust2_signaling + 1) % SIGNAL_TIME
       """ 
        print(Recivers[0].Data_result)
        cust1_signal_rate = (cust1_signal_rate + 1) % SIGNAL_RATE
        cust2_signal_rate = (cust2_signal_rate + 1) % SIGNAL_RATE
    print(Recivers[0].Data_result)
        
    
