import numpy as np
import random

class Reciver:
    def __init__(self,pos_x,pos_y, Signal_radius):
        self.Data_result = []               #hold recived signals
        self.Pos = (pos_x,pos_y)            #Position of reciver in world
        self._Signal_radius = Signal_radius #How far the signal can be recived
        self._time_index = 0                #Index for data array logic 

    def append_signal(self, cust_id, cust_pos):
        """
        This function addes the recived signals to the data array of the
        reciver
            cust_id = id of signal from customer, i.e. customer 1 has id 1
            cust_pos = position of customer when sending signal
        """
        
        tmp = [(cust_id,self._distance(cust_pos))] #The signal id
        if len(self.Data_result) == 0: #if first signal to be recived
            self.Data_result += tmp

        #Add signal to array if signal in signal radius
        elif self._distance(cust_pos) <= self._Signal_radius:
            if len(self.Data_result) == self._time_index:
                self.Data_result += tmp
            else:
                print("OVERLAP IN SIGNAL")
                self.Data_result[self._time_index] = 0

    def __str__(self):
        return str(self.Pos)

    def __repr__(self):
        return self.__str__()

    def clear_signal(self, ts_1, ts_2):
        pass

    def _distance(self, cust_pos): 
        """
        This function calculates the distance the signal propigates 
        using pythagoran formula
        """
        return np.sqrt((cust_pos[0] - self.Pos[0])**2 + (cust_pos[1] - self.Pos[1])**2)
    
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

#
# def drawCellTowers():
#     x1 = int(str(Recivers)[2])
#     y1 = int(str(Recivers)[5])
#     x2 = int(str(Recivers)[10])
#     y2 = int(str(Recivers)[13])
#     x3 = int(str(Recivers)[18])
#     y3 = int(str(Recivers)[21])
#     x = random.randint(1, 4)
#     y = random.randint(1, 4)
#     # print(x, y)
#     r1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
#     r2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
#     r3 = ((x - x3) ** 2 + (y - y3) ** 2) ** 0.5
#     return x1,y1,r1,x2,y2,r2,x3,y3,r3

def est_Pos(Reciver1,Reciver2,Reciver3):
    x1 = Reciver1.Pos[0]
    y1 = Reciver1.Pos[1]
    x2 = Reciver2.Pos[0]
    y2 = Reciver2.Pos[1]
    x3 = Reciver3.Pos[0]
    y3 = Reciver3.Pos[1]
    # x = random.random()*10
    # y = random.random()*10
    x = random.randrange(3, 5)
    y = random.randrange(5, 6)
    # x = 4
    # y = 3
    print(x, y)
    r1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    r2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
    r3 = ((x - x3) ** 2 + (y - y3) ** 2) ** 0.5
    # -----Triliteration CODE ------
    A = 2*x2 - 2*x1
    B = 2*y2 - 2*y1
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2*x3 - 2*x2
    E = 2*y3 - 2*y2
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
    x0 = (C*E - F*B) / (E*A - B*D)
    y0 = (C*D - A*F) / (B*D - A*E)
    return x0, y0

def Update_recivers(Recivers):
    for i in  range(len(Recivers)):
        Recivers[i].update()

def Init_Recivers(N,ts):
    Recivers = [0]*N
    for i in range(0,N):
        Recivers[i] = Reciver(random.randrange(1,50),random.randrange(1,50),ts)
    print(str(Recivers))
    return Recivers

"""
def Append_signal_to_recivers(Recivers,Customer)
    for i in range(len(Recivers)):
        Recivers[i].append_signa(Customer.id, Customer.pos)
"""

if __name__ == "__main__":
    random.seed(2)
    N = 5
    SIGNAL_RATE = 8 #How long time passes between signals
    SIGNAL_TIME = 3 #How long each signal lasts, transmission time
    SIGNAL_STRENGHT = 100 #Radius of reciver signaling space


    Recivers = Init_Recivers(N,SIGNAL_STRENGHT)
    m, y = est_Pos(Recivers[0],Recivers[1],Recivers[2])
    print(m)
    print(y)
    #Customers = Spawn_customer()

    cust1_signal_rate = 2
    cust1_signaling = 0

    cust2_signal_rate = 3
    cust2_signaling = 0
    
    for i in range(0,20):
        
        print(i)
        if cust1_signal_rate == 0 or cust1_signaling > 0:
            print("CUST 1 SIGNALING")
            # print("----------")
            for j in range(0, N):
                Recivers[j].append_signal(1, (2, 3))
            # print("----------")

            #Rcivers[0].append_signal(Cust[0].id, Cust[0].pos)
            # Recivers[0].append_signal(1,(2,3))
            cust1_signaling = (cust1_signaling + 1) % SIGNAL_TIME
        """ 
        if cust2_signal_rate == 0 or cust2_signaling > 0:
            print("CUST 2 SIGNALING")
            for k in range(0, N):
                Recivers[k].append_signal(2,(5,5))
            cust2_signaling = (cust2_signaling + 1) % SIGNAL_TIME
        """
        
        Update_recivers(Recivers)
        #update_customers(Customers)
        cust1_signal_rate = (cust1_signal_rate + 1) % SIGNAL_RATE
        cust2_signal_rate = (cust2_signal_rate + 1) % SIGNAL_RATE
    for m in range(0, N):
        print(Recivers[m].Data_result)



