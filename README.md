# Localization of The SmartCart
This code is for simulation of the trilateration of the SmartCart system, which utilizes
a sound positioning system.

# Install and Run

The simulation is run using Python 2.7 - Python 3.6
However, the following packages are needed to run the simulation:

~~~~
Numpy
Matplotlib
Random
~~~~

To run the simulation, the "main.py" file is run. This can be done using your preferred software, e.g. Visual Studio Code, or using following command in terminal:

~~~~
python main.py
~~~~

The program will then run with the saved parameters in the file "parameters.py"


# Simulation

The parameters for the simulation are located in the "parameters.py" file.
The parameters are divided into 4 groups, Shop, Path, Recivers, and Customers

#### Shop ####
The parameters in the shop group hold the information of the desired shop setup such as dimensions.

#### Path ####
The parameters in the path catgory are for the random generation of the paths. In this catagory there are parameters like the path time and gaussian distribution of the path generation.

#### Recivers ####
The parametrs in this catagory is the settings for the spawning of the recivers in the shop, for example the range of the recivers and spacing between each reciver.

#### Customers ####
The parameters in this group is for settings of the customers in the simulation. Here parameters like the number of customers in and the transmisson rate and signal time are located.
*Note:*

#### Recomended parameters ####

The parameters that have the most considerable effect on the simulation are the parameters for the Receivers, that is, R_range and R_spacing,
and the parameters for the customers, NUMBER_OF_CUSTOMERS, SIGNAL_RATE, SIGNAL_TIME & SIGNAL_STRENGTH.

We recommend running the simulation with the following parameters:


- For the visualization of 1 customers
~~~~
R_range = 10
R_spacing = 1
NUMBER_OF_CUSTOMERS = 1
SIGNAL_RATE = 2000.0 
SIGANL_TIME = 40 ms
SIGNAL_STRENGTH = 10
~~~~

- For visualizations of signal conflicts
~~~~
R_range = 25
R_spacing = 0.5
NUMBER_OF_CUSTOMERS = 4
SIGNAL_RATE = 600
SIGNAL_TIME = 300
SIGNAL_STRENGTH = 20
~~~~
