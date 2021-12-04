from Customer import *
from Path import *
from Reciver import *
from matplotlib.pylab import (figure, plot, xlabel, ylabel, legend, title, subplots, show, boxplot,bar,xlim,ylim)
import random
import time
import math
import matplotlib.pyplot as plt
import numpy as np

from parameters import *


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
    try :
        x0 = (C*E - F*B) / (E*A - B*D) + random.uniform(0,1)
        y0 = (C*D - A*F) / (B*D - A*E) + random.uniform(0,1)
        if (x0 > S_XMAX or x0 < 0) or (y0 > S_YMAX or y0 < 0):
            return float('inf'),float('inf')
        else:
            return x0, y0
    except:
        return float('inf'),float('inf')


def Update_recivers(Recivers):
    for i in  range(len(Recivers)):
        Recivers[i].update()

def Init_Recivers(ts):
    # create receivers
    recivers = [];
    # place receivers around the shop
    k = -1;
    n_rows = math.ceil((S_YMAX - 2*R_Border) / (math.sqrt(3)/2*R_Range*R_Spacing));
    n_cols = math.ceil((S_XMAX - 2*R_Border) / (R_Range*R_Spacing) + 0.5);
    yplaceRange = np.arange(n_rows + 1) * ((S_YMAX - 2*R_Border) / n_rows) + R_Border;
    xplaceRange = np.arange(n_cols + 1) * ((S_XMAX - 2*R_Border) / (n_cols + 0.5)) + R_Border;
    
    for yplace in yplaceRange:
        k += 1;
        for xplace in xplaceRange:
            r = Reciver(ts);
            if k % 2 == 1:
                r.Pos[0] = xplace + ((S_XMAX - 2*R_Border) / (n_cols + 0.5))/2;
            else:
                r.Pos[0] = xplace;
            r.Pos[1] = yplace;
            recivers.append(r);
    
    return recivers

def Init_Customers(N,signal_rate):
    # create customers
    customers = [];
    for cust_idx in range(N):
        p = Path()
        c = Customer(p.path,cust_idx,signal_rate);
        customers.append(c);
    return customers


def find_recivers(Recivers,cust_id):
    tmp = []
    if len(Recivers) < 3:
        return tmp
    for i in range(len(Recivers)):
        if type(Recivers[i].Data_result[-1]) is tuple and Recivers[i].Data_result[-1][0] == cust_id:
            tmp.append(i)
        if len(tmp) == 3:
            r1_pos = Recivers[tmp[0]].Pos
            r2_pos = Recivers[tmp[1]].Pos
            r3_pos = Recivers[tmp[2]].Pos

            if r1_pos[0] == r2_pos[0] and r1_pos[0] == r3_pos[0]:
                tmp = tmp[0:-1]
            elif r1_pos[1] == r2_pos[1] and r1_pos[1] == r3_pos[1]:
                tmp = tmp[0:-1]
            else:
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
    #print(path[1])
    #for i in range(0,len(path[0])-1):
    for i in range(0,len(est[0])):
        x_diff = path[0][i] - est[0][i]
        y_diff = path[1][i] - est[1][i]
        tmp.append(np.sqrt(x_diff**2 + y_diff**2))
    return tmp

def get_reciver_pos(Recivers):
    x_tmp = []
    y_tmp = []
    for i in range(len(Recivers)):
        x_tmp.append(Recivers[i].Pos[0])
        y_tmp.append(Recivers[i].Pos[1])
    return [x_tmp,y_tmp]

def ShowShop(customers, receivers, showReceivers = True):
    
    # plot
    for c in customers:
        plt.figure(dpi=1200);
        plt.axis([0, S_XMAX, 0, S_YMAX])
        path_x,path_y = split_axis(c.PATH)
        plt.plot(path_x, path_y)
    
        # receivers
        if showReceivers == True:
            x = [];
            y = [];
            for r in receivers:
                x.append(r.Pos[0]);
                y.append(r.Pos[1]);
            plt.scatter(x, y, marker='1', c = '#FF0000')
        
    


if __name__ == "__main__":

    
    Recivers = Init_Recivers(SIGNAL_STRENGHT)
    Customers = Init_Customers(NUMBER_OF_CUSTOMERS,SIGNAL_RATE)


    time = 0
    time_axis = []


    ## BEGIN SIMULATION, reseloutin of sim is P_R ##
    print("Simulating SmartCart with resoulution of " + str(P_R) + " s:")
    print("\tNr. Customers: " + str(NUMBER_OF_CUSTOMERS))
    print("\tNr. Recivers: " + str(len(Recivers)))
    for i in range(0,P_Length):
        time = i *P_R
        time_axis.append(time)
        for Customer in Customers:
            if Customer.END and not Customer.left:
                #print("Customer " + str(Customer.id) + " leaves")
                Customer.left = True

            if Customer.is_signaling():
                #print("%7.4f s: Customer 0 signals" %(time))
                for j in range(0, len(Recivers)):
                    Recivers[j].append_signal(Customer.id,Customer.cur_pos )
        
            # Perform the triliatation 
            if not Customer.END and not Customer.is_signaling() and Customer.signal_cycle == SIGNAL_TIME - 1: 
                #print("Performing trilateration")
                reciver_index  = find_recivers(Recivers,Customer.id)
                #print(len(reciver_index))
                if len(reciver_index) ==  3:
                    r1,r2,r3 = reciver_index
                    Customer.append_est_pos(est_Pos(Recivers[r1],Recivers[r2],Recivers[r3]))
                    print("""%7.4f s: Customer %1.0f real pos: (%2.2f, %2.2f)
              Customer %1.0f est pos: (%2.2f, %2.2f) """
                        %(time,Customer.id,Customer.cur_pos[0],Customer.cur_pos[1],
                            Customer.id, Customer.est_pos[-1][0],Customer.est_pos[-1][1]))

            # Update customers and recived data in recivers
            Customer.move()
            Customer.update(SIGNAL_RATE, SIGNAL_TIME)
    
        Update_recivers(Recivers)
    print("END of simulation")
    


    if len(Customers) < 5:
        i=0
        ## calculating the results from simulation and plot.##
        fig1, axs1 = subplots(NUMBER_OF_CUSTOMERS, figsize=(10,10))
        fig1.tight_layout()
        
        fig2, axs2 = subplots(NUMBER_OF_CUSTOMERS, figsize=(10,10))
        fig2.tight_layout()
    
        fig3, axs3 = subplots(NUMBER_OF_CUSTOMERS, figsize=(10,10))
        fig3.tight_layout()

        fig4, axs4 = subplots(NUMBER_OF_CUSTOMERS, figsize=(10,10))
        fig4.tight_layout()
    
        if len(Customers) == 1:

            path_x,path_y = split_axis(Customers[0].PATH)
            est_x,est_y = split_axis(Customers[0].est_pos)
            residual_error = calc_diff([path_x,path_y],[est_x,est_y])
            reciver_pos_x, reciver_pos_y = get_reciver_pos(Recivers)
        
        
            axs1.plot(path_x[0:len(time_axis)],path_y[0:len(time_axis)],'-',est_x,est_y,'o',reciver_pos_x,reciver_pos_y,'x')
            axs1.set_xlabel("x coordinates [m]")
            axs1.set_ylabel("y coordinates [m]")
            axs1.legend(['Real val','Est val','Reciver'])
            axs1.set_title('Customer ' + str(Customers[0].id)) 
            
            axs2.plot(time_axis,path_x[0:len(time_axis)],'-',time_axis,est_x,'o')
            axs2.set_xlabel("Time [sec]")
            axs2.set_ylabel("x coordinates [m]")
            axs2.legend(['Real val','Est val'])

        
            axs3.plot(time_axis,path_y[0:len(time_axis)],'-',time_axis,est_y,'o')
            axs3.set_xlabel("Time [sec]")
            axs3.set_ylabel("y coordinates [m]")
            axs3.legend(['Real val','Est val'])
    

        
            axs4.plot(time_axis[0:len(residual_error)],residual_error,[0,np.max(time_axis)],[np.mean(residual_error)]*2)
            axs4.set_xlabel("Time [m]")
            axs4.set_ylabel("Residual error [m]")
            axs4.legend(['Residual error','Mean Residual error'])

            print("Customer: " + str(Customers[0].id))
            print("\tMean residual error: " + str(np.mean(residual_error)))
            print("\tMax error: " + str(np.max(residual_error)))
    
        else:
            for customer in Customers:
                path_x,path_y = split_axis(customer.PATH)
                est_x,est_y = split_axis(customer.est_pos)
                residual_error = calc_diff([path_x,path_y],[est_x,est_y])
                reciver_pos_x, reciver_pos_y = get_reciver_pos(Recivers)
        
        
                axs1[i].plot(path_x[0:len(time_axis)],path_y[0:len(time_axis)],'-',est_x,est_y,'o',reciver_pos_x,reciver_pos_y,'x')
                axs1[i].set_xlabel("x coordinates [m]")
                axs1[i].set_ylabel("y coordinates [m]")
                axs1[i].legend(['Real val','Est val','Reciver'])
                axs1[i].set_title('Customer ' + str(customer.id))
        
        
                axs2[i].plot(time_axis,path_x[0:len(time_axis)],'-',time_axis,est_x,'o')
                axs2[i].set_xlabel("Time [sec]")
                axs2[i].set_ylabel("x coordinates [m]")
                axs2[i].legend(['Real val','Est val'])

        
                axs3[i].plot(time_axis,path_y[0:len(time_axis)],'-',time_axis,est_y,'o')
                axs3[i].set_xlabel("Time [sec]")
                axs3[i].set_ylabel("y coordinates [m]")
                axs3[i].legend(['Real val','Est val'])
    

        
                axs4[i].plot(time_axis[0:len(residual_error)],residual_error,[0,np.max(time_axis)],[np.mean(residual_error)]*2)
                axs4[i].set_xlabel("Time [sec]")
                axs4[i].set_ylabel("Residual error [m]")
                axs4[i].legend(['Residual error','Mean Residual error'])

                print("Customer: " + str(customer.id))
                print("\tMean residual error: " + str(np.mean(residual_error)))
                print("\tMax error: " + str(np.max(residual_error)))
                i += 1
    else:
        data = []
        nr_of_est_points = []
        cust_id = range(1,len(Customers)+1)
        for cust in Customers:
            path_x,path_y = split_axis(cust.PATH)
            est_x,est_y = split_axis(cust.est_pos)
            residual_error = calc_diff([path_x,path_y],[est_x,est_y])
            data.append(residual_error)
            
            nr_of_est_points.append(len(set(cust.est_pos)))

        
        best_cust_indx = nr_of_est_points.index(max(nr_of_est_points))
        worst_cust_indx = nr_of_est_points.index(min(nr_of_est_points))
    
        best_cust = Customers[best_cust_indx]
        worst_cust = Customers[worst_cust_indx]
        
        fig = figure(figsize = (10,7))
        boxplot(data)
        xlabel("Customers")
        ylabel("Residual error [m]")

        fig = figure(figsize = (10,7))
        bar(cust_id,nr_of_est_points)
        title("Number of estimated positions")
        xlabel("Customers")
        ylabel("Estimated positions")

        fig = figure(figsize = (10,7))
        bar(cust_id,((np.array(nr_of_est_points)-1)/(P_Time*1000/SIGNAL_RATE))*100)
        title("Ratio of est. pos and nr. of sent signals")
        xlabel("Customers")
        ylabel("Ratio [%]")

        fig1, axs1 = subplots(2, figsize=(10,10))
        fig1.tight_layout()
        
        i = 0
        title = ["Best customer", "Worst customer"]
        for cust in [best_cust, worst_cust]:
            path_x,path_y = split_axis(cust.PATH)
            est_x,est_y = split_axis(cust.est_pos)
            reciver_pos_x, reciver_pos_y = get_reciver_pos(Recivers)

            axs1[i].plot(path_x[0:len(time_axis)],path_y[0:len(time_axis)],'-',est_x,est_y,'o',reciver_pos_x,reciver_pos_y,'x')
            axs1[i].set_xlabel("x coordinates")
            axs1[i].set_ylabel("y coordinates")
            axs1[i].legend(['Real val','Est val','Reciver'])
            axs1[i].set_title(title[i])
            i += 1

    plt.show()

