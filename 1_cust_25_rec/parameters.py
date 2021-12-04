import math
import numpy as np

# Shop
S_XMAX = 40; # max X size of a shop (width)
S_YMAX = 30; # max Y size of a shop (hight)
S_XE = 5; # entrance X coordinate
S_YE = 0; # entrance Y coordinate
S_R = 0.01; # shop resolution in meters # 0.01m = 1cm

# Path
P_Time = 10*60; # time spend by customer in shop in seconds
P_R = 0.01; # path time resolution in seconds
P_Length = int(P_Time / P_R); # how many points path consists of

P_SGMean = 0.75; # mean of a gauss distribution for customer speed m/s
P_SGStd = 0.50; # std of a gauss distribution for customer speed m/s
P_SMin = 0; # minimum linear speed
P_SMax = 0.5; # maximum linear speed

P_Hold = 7; # hold the current direction for next few moves
P_DirChangeFact = 0.02; # how much direction changes each time
P_DirMin = -0.98*math.pi; # max left angle
P_DirMax = math.pi; # max right angle

# Receiver
R_Range = 10; # maximum range in meters
R_Spacing = 1; # percentage of maximum range
R_Res = 0.001; # resolution in sec 0.001s = 1ms
R_Border = 1; # border width [m] where there are no receivers

# Customers
NUMBER_OF_CUSTOMERS = 1; # number of customers
SIGNAL_RATE = 2000.0  #How long time passes between signals, ms
SIGNAL_TIME = 40  #How ling each signal lasts, transmisson time, ms
SIGNAL_STRENGHT = 10 #Radius of reciver signaling space
