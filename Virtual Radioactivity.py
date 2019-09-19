# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import random


###########################################################
# VIRTUAL RADIOACTIVITY EXPERIMENT
###########################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Section 1 - Experiment Set Up

totalNumberOfAtoms =   1000   #Enter a number - remember a large enough number will show a clearer pattern 
probabilityLevel =  0.18   #The chance of each atom decaying, try using a small decimal (0.1 for instance)
#Remember that the probability level shows the chance of an atom decaying for any time period you want - 
#you could have it per second, hour, day or even year depending on what element you want to simulate.
atoms = np.ones(totalNumberOfAtoms)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Section 2 - Data Recording Set Up

timepassed = 100   #Amount of timesteps set to pass

timeStepArray = np.zeros(timepassed)
numberOfActiveAtomsArray = np.zeros(timepassed)

#These blank arrays are going to be used later on. An array is just a list of numbers, and are an important
#part of coding - especially in science!

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Section 3 - Running The Experiment

for i in range(timepassed): #This is a for loop, and is a repeated command. Here, it is being repeated
                            #however long the timepassed value was set to - 100 is the default setting

    timeStepArray[i] = i 

    numberOfActiveAtoms = np.sum(atoms)
    numberOfActiveAtomsArray[i] = numberOfActiveAtoms


    for j in range(totalNumberOfAtoms):
        randomlyGeneratedNumber = random.uniform(0, 1)

        if(randomlyGeneratedNumber <= probabilityLevel):
            atoms[j] = 0

#This section randomly chooses a number between 0 and 1 for each atom at each timestep, and if that number is below the
#level you set earlier, the atom will decay. This should create our "half-life" decay, and we can check this by plotting
#the results on a graph
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Section 4 - Presenting The Raw Data

plt.figure(1)
plt.title('Graph To Show Decay Of ' + str(totalNumberOfAtoms) + ' Atoms')
plt.xlabel('Time Steps')
plt.ylabel('Number Of Undecayed Atoms')

plt.plot(timeStepArray, numberOfActiveAtomsArray, 'o')
plt.show()

#The "plt." prefix here is used to create graphs and plots, and is using the pyplot package we imported at the top.
#This will create a plot showing the number of undecayed atoms at each timestep, and should follow a curve.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Section 5 - Creating A Model
#
# The below function is created from the equation of radioactive decay.

def TheoreticalDecay(timeArray, totalNumberOfAtoms, decayConstant):

    expectedNumberOfActiveAtomsArray = totalNumberOfAtoms * np.exp(-decayConstant * timeArray)

    return expectedNumberOfActiveAtomsArray


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Section 5 - Fitting The Model To Raw Data

#Now all we need to do is create another plot, combining the experimental data we created before with
#what we have created in our model. If the model was correct, it should create a line that fits the data closely!

plt.figure(2)
plt.title('Graph To Show Decay Analysis Of ' + str(totalNumberOfAtoms) + ' Atoms')
plt.xlabel('Time Steps')
plt.ylabel('Number Of Undecayed Atoms')

timeArray = np.linspace(timeStepArray[0], timeStepArray[-1], 5000)

expectedNumberOfActiveAtomsArray = TheoreticalDecay(timeArray, totalNumberOfAtoms, probabilityLevel)
popt, pcov = curve_fit(
                    TheoreticalDecay,
                    timeStepArray, numberOfActiveAtomsArray,
                    (totalNumberOfAtoms, 0.5))
                    
                    
plt.plot(timeStepArray, numberOfActiveAtomsArray, 'o', label = 'Raw Data')
plt.plot(timeArray, TheoreticalDecay(timeArray, totalNumberOfAtoms, popt[1]), label = 'Theoretical Model')

plt.legend(loc = 'best')
plt.show()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Section 6 - Extracting Key Information

print ('-------------------------------------------------')
print ('Decay constant = ' + str(popt[1]))

decayHalfLife = np.log(2) / popt[1]

print ('Decay half-life = ' + str(decayHalfLife))
print ('-------------------------------------------------')

#The decay constant shows the proportion of atoms that will decay at each timestep, taken from the model.
#It should be very close to what you set at the start of the code as the probability.

#The half-life is the amount of time taken for half of the atoms to decay. It should remain constant 
#no matter how many atoms there are, as long as the decay constant remains the same. Why not try
#different numbers of atoms to test this?