# Localisation of The SmartCart
This code is for simulation of the trilateration of the SmartCart system, which utilises
a sound positioning system.

# Install and Run

The simulation is run using Python 2.7 - Python 3.6
However, the following packages are needed to run the simulation:

~~~~
Numpy
Matplotlib
Random
~~~~

To run the simulation, the "main.py" file is run. This can be done using your preferred software, e.g. Visual Studio Code, or using the following command in the terminal:

~~~~
python main.py
~~~~

The program will then run with the saved parameters in the file "parameters.py"


# Simulation

The parameters for the simulation are located in the "parameters.py" file.
The parameters are divided into four groups, Shop, Path, Receivers, and Customers.

#### Shop ####
The parameters in the shop group hold the information of the desired shop setup, such as dimensions.

#### Path ####
The parameters in the path category are for the random generation of the paths. So in this category, there are parameters like the path time and gaussian distribution of the path generation.

#### Receivers ####
The parameters in this category are the settings for spawning the receivers in the shop, for example, the range of the receivers and spacing between each receiver.

#### Customers ####
The parameters in this group are for the settings of the customers in the simulation. Here parameters like the number of customers in and the transmission rate and signal time are located.

*Note: parameter "SIGNAL_RATE" needs to be a float*

#### Recommended parameters ####

The parameters that have the most considerable effect on the simulation are the parameters for the Receivers, that is, R_range and R_spacing,
and the parameters for the customers, NUMBER_OF_CUSTOMERS, SIGNAL_RATE, SIGNAL_TIME & SIGNAL_STRENGTH.

We recommend simulating with the following parameters:


- For the visualisation of 1 customer
~~~~
R_range = 10
R_spacing = 1
NUMBER_OF_CUSTOMERS = 1
SIGNAL_RATE = 2000.0 
SIGANL_TIME = 40 ms
SIGNAL_STRENGTH = 10
~~~~

- For visualisations of 4 customers
~~~~
R_range = 10
R_spacing = 1
NUMBER_OF_CUSTOMERS = 4
SIGNAL_RATE = 2000.0
SIGNAL_TIME = 40
SIGNAL_STRENGTH = 10
~~~~

- For visualisation of 4 customers with optimised SIGNAL_RATE
~~~~
R_range = 10
R_spacing = 1
NUMBER_OF_CUSTOMERS = 4
SIGNAL_RATE = 2000.0
SIGNAL_TIME = 10
SIGNAL_STRENGTH = 10
~~~~

- For visualisation of 16 customers
~~~~
R_range = 10
R_spacing = 1
NUMBER_OF_CUSTOMERS = 16
SIGNAL_RATE = 2000.0
SIGNAL_TIME = 40
SIGNAL_STRENGTH = 10
~~~~
