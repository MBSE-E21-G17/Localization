import numpy as np
import random as rand


class test:
    def __init__(self, pos_x, pos_y, Signal_radius):
        self.Data_result = []  # hold recived signals
        self.Pos = (pos_x, pos_y)  # Position of reciver in world
        self._Signal_radius = Signal_radius  # How far the signal can be recived
        self._time_index = 0  # Index for data array logic

    def append_signal(self, cust_id, cust_pos):
        """
        This function addes the recived signals to the data array of the
        reciver
            cust_id = id of signal from customer, i.e. customer 1 has id 1
            cust_pos = position of customer when sending signal
        """

        tmp = [cust_id]  # The signal id
        if len(self.Data_result) == 0:  # if first signal to be recived
            self.Data_result += tmp

        # Add signal to array if signal in signal radius
        elif self._distance(cust_pos) <= self._Signal_radius:
            if len(self.Data_result) == self._time_index:
                self.Data_result += tmp
            else:
                print("OVERLAP IN SIGNAL")
                self.Data_result[self._time_index] = 0

    def clear_signal(self, ts_1, ts_2):
        pass

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

    # def trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3):
    #   A = 2*x2 - 2*x1
    #   B = 2*y2 - 2*y1
    #   C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    #   D = 2*x3 - 2*x2
    #   E = 2*y3 - 2*y2
    #   F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
    #   x = (C*E - F*B) / (E*A - B*D)
    #   y = (C*D - A*F) / (B*D - A*E)
    #   return x,y
    #
    # def receiverTowers():
    #     x1 = rand.randint(-150, -80)
    #     y1 = rand.randint(-150, 150)
    #     x2 = rand.randint(80, 150)
    #     y2 = rand.randint(20, 150)
    #     x3 = rand.randint(80, 150)
    #     y3 = rand.randint(-150, -20)
    #     x = rand.randint(-60, 60)
    #     y = rand.randint(-60, 60)
    #     r1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    #     r2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
    #     r3 = ((x - x3) ** 2 + (y - y3) ** 2) ** 0.5


def Update_recivers(Recivers):
    for i in range(len(Recivers)):
        Recivers[i].update()


def Init_Recivers(N, ts):
    Recivers = [0] * N
    for i in range(0, N):
        Recivers[i] = (rand.randrange(0, 5), rand.randrange(0, 5), 50)
        print("***********")
        print(Recivers[i])
        # for x in Recivers:
        # for y in x:
        #     print(Reciver[i])
        print("***********")

    return Recivers


if __name__ == "__main__":

    rand.seed(2)
    N = 5
    SIGNAL_RATE = 8  # How long time passes between signals
    SIGNAL_TIME = 3  # How long each signal lasts, transmission time
    SIGNAL_STRENGHT = 100  # Radius of reciver signaling space

    Recivers = Init_Recivers(N, SIGNAL_STRENGHT)
    cust1_signal_rate = 2
    cust1_signaling = 0

    cust2_signal_rate = 3
    cust2_signaling = 0

    for i in range(0, 20):

        print(i)
        if cust1_signal_rate == 0 or cust1_signaling > 0:
            print("CUST 1 SIGNALING")
            Recivers[0].append_signal(1, (2, 3))
            cust1_signaling = (cust1_signaling + 1) % SIGNAL_TIME

        if cust2_signal_rate == 0 or cust2_signaling > 0:
            print("CUST 2 SIGNALING")
            Recivers[0].append_signal(2, (2, 3))
            cust2_signaling = (cust2_signaling + 1) % SIGNAL_TIME
        Update_recivers(Recivers)
        cust1_signal_rate = (cust1_signal_rate + 1) % SIGNAL_RATE
        cust2_signal_rate = (cust2_signal_rate + 1) % SIGNAL_RATE
    print(Recivers[0].Data_result)

