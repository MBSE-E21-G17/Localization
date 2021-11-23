from Customer import *
from Path import *
from Reciver import *
from matplotlib.pylab import (figure, plot, xlabel, ylabel, legend, title, subplot, show)
import random
import time
import matplotlib.pyplot as plt
import numpy as np


def est_Pos(Reciver1,Reciver2,Reciver3):
    x1 = Reciver1.Pos[0]
    y1 = Reciver1.Pos[1]
    x2 = Reciver2.Pos[0]
    y2 = Reciver2.Pos[1]
    x3 = Reciver3.Pos[0]
    y3 = Reciver3.Pos[1]
    
    
    r1 = Reciver1.Data_result[-1][1]
    r2 = Reciver2.Data_result[-1][1]
    r3 = Reciver3.Data_result[-1][1]
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

def Init_Recivers(N,ts,width,height):
    Recivers = [0]*N
    for i in range(0,N):
        Recivers[i] = Reciver(random.randrange(0,width),random.randrange(0,height),ts)
    print(str(Recivers))
    return Recivers


def find_recivers(Recivers,cust_id):
    tmp = []
    for i in range(len(Recivers)):
        print(type(Recivers[i].Data_result[-1]))
        if type(Recivers[i].Data_result[-1]) is tuple and Recivers[i].Data_result[-1][0] == cust_id:
            tmp.append(i)
        if len(tmp) == 3:
            return tmp
    return tmp

def split_axis(data):
    x = []
    y = []
    for i in range(0,len(data)):
        x.append(data[i][0])
        y.append(data[i][1])
    return [x,y]

def calc_diff(path,est):
    tmp = []
    for i in range(0,len(path[0])):
        x_diff = path[0][i] - est[0][i]
        y_diff = path[1][i] - est[1][i]
        
        print("path: (%2.1f, %2.1f)" %(path[0][i],path[1][i]))
        print("est: (%2.1f, %2.1f)" %(est[0][i],est[1][i]))
        print("Error: " + str(np.sqrt(x_diff**2 + y_diff**2)) + "\n")
        tmp.append(np.sqrt(x_diff**2 + y_diff**2))
    return tmp

def get_reciver_pos(Recivers):
    x_tmp = []
    y_tmp = []
    for i in range(len(Recivers)):
        x_tmp.append(Recivers[i].Pos[0])
        y_tmp.append(Recivers[i].Pos[1])
    return [x_tmp,y_tmp]


random.seed(2)
STORE_HEIGHT = 20
STORE_WIDTH = 20
NUMBER_OF_RECIVERS = 30
NUMBER_OF_CUSTOMERS = 1
SIGNAL_RATE = 3 #How long time passes between signals
SIGNAL_TIME = 2 #How long each signal lasts, transmission time
SIGNAL_STRENGHT = 20 #Radius of reciver signaling space
SIM_TIME = 20

Recivers = Init_Recivers(NUMBER_OF_RECIVERS,SIGNAL_STRENGHT,STORE_HEIGHT,STORE_WIDTH)
Customers = [Customer(random.sample(Path.path, 1),1)]

time = 0
time_axis = []


## BEGIN SIMULATION ##
print("%7.4f s: Customer 0 arraives" %(time))

for i in range(0,SIM_TIME):
    time += i
    time_axis.append(time)
    if Customers[0].END and not Customers[0].left:
        print("Customer 0 leaves")
        Customers[0].left = True

    if Customers[0].is_signaling():
        print("%7.4f s: Custmer 0 signals" %(time))
        for j in range(0, NUMBER_OF_RECIVERS):
            Recivers[j].append_signal(Customers[0].id,Customers[0].cur_pos )
    
    # Perform the triliatation 
    if not Customers[0].END and not Customers[0].is_signaling() and Customers[0].signal_cycle == SIGNAL_TIME - 1: # -1 ???
        print("Performing trilateration")
        reciver_index  = find_recivers(Recivers,Customers[0].id)
        if len(reciver_index) ==  3:
            r1,r2,r3 = reciver_index
            Customers[0].append_est_pos(est_Pos(Recivers[r1],Recivers[r2],Recivers[r3]))
            print("""%7.4f s: Customer 0 real pos: (%2.2f, %2.2f)
           Customer 0 est pos: (%2.2f, %2.2f) """
                %(time,Customers[0].cur_pos[0],Customers[0].cur_pos[1],
                  Customers[0].est_pos[-1][0],Customers[0].est_pos[-1][1]))

    # Update customers and recived data in recivers
    Customers[0].move()
    Update_recivers(Recivers)
    Customers[0].update(SIGNAL_RATE, SIGNAL_TIME)

print("END of simulation")



## calculating the results from simulation and plot.##
path_x,path_y = split_axis(Customers[0].PATH)
est_x,est_y = split_axis(Customers[0].est_pos)
residual_error = calc_diff([path_x,path_y],[est_x,est_y])
reciver_pos_x, reciver_pos_y = get_reciver_pos(Recivers)

figure(1)
plot(path_x,path_y,'-',est_x,est_y,'o',reciver_pos_x,reciver_pos_y,'x')
xlabel("x coordinates")
ylabel("y coordinates")
legend(['Real val','Est val','Reciver'])

figure(2)
plot(time_axis[0:len(path_x)],path_x,'-',time_axis[0:len(est_x)],est_x,'o')
xlabel("Time")
ylabel("x coordinates")
legend(['Real val','Est val'])

figure(3)
plot(time_axis[0:len(path_y)],path_y,'-',time_axis[0:len(est_y)],est_y,'o')
xlabel("Time")
ylabel("y coordinates")
legend(['Real val','Est val'])


figure(4)
plot(time_axis[0:len(residual_error)],residual_error)
xlabel("Time")
ylabel("Residual error")



print("Mean residual error: " + str(np.mean(residual_error)))
print("Max error: " + str(np.max(residual_error)))

##Print data of recivers, DEBUG!!##
"""
for i in range(len(Recivers)):
    print(Recivers[i].Data_result)
"""
plt.show()






