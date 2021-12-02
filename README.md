# Localization of The SmartCart
This code is for simulation of the trilateration of the SmartCart system, which utilizes
a sound positioning system.

#Install and Run

The simulation is run using Python 2.7 --Python 3.6
However, the following pachages are needed to run the simulation:

~~~~
Numpy
Matplotlib
Random
~~~~

To run the simulation, run the main.py. 

#Simulation

The parameters for the simulation are located in the parameters.py file. 
The parameters that have the most considerable effect on the simulation are the parameters for the Receivers, that is, R_range and R_spacing,
and the parameters for the customers, NUMBER_OF_CUSTOMERS, SIGNAL_RATE, SIGNAL_TIME & SIGNAL_STRENGTH.

We recomend to run the simulation with the following paramters:


-for maximum number of customers for working system
~~~~
R_range = 25
R_spacing = 0.5
NUMBER_OF_CUSTOMERS = 10
SIGNAL_RATE = 600
SIGANL_TIME = 300
SIGNAL_STRENGTH = 20
~~~~

-For vizulation of signal conflicts
~~~~
R_range = 25
R_spacing = 0.5
NUMBER_OF_CUSTOMERS = 4
SIGNAL_RATE = 600
SIGNAL_TIME = 300
SIGNAL_STRENGTH = 20
~~~~
