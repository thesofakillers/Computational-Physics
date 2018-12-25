'''This module simulates the progression the 225Ra-->225Ac-->221Fr Decay Chain
using analytical, ODE and Monte-Carlo approaches.'''

from __future__ import division

import numpy
import random
import matplotlib.pyplot as pyplot
import scipy.integrate

USER = 'Giulio Starace'
USER_ID = 'dzgf42'

t_half_rad = 20.8 #Half life of 225Ra (days)
t_half_act = 10.0 #Half life of 225Ac (days)
N0 = 250 #initial number of 225Ra atoms
t1 = 100 #end time of simulation
n_time = 50 #number of timepoints to solve to
TAU_Ra = t_half_rad/(numpy.log(2))
TAU_Ac = t_half_act/(numpy.log(2))

# Array of times used for plotting & analytical solution
ts = numpy.arange(0, t1, (t1/n_time))

# returns numpy array of 225Ra Atoms at specified times using analytical sol'n
def analytic(N0, timebase):
    return N0 * numpy.exp(-timebase/TAU_Ra)

# returns 2D array of 225Ra and 225Ac atoms at speified times using MC method
def monte_carlo_sim(N0, t1, n_time):
    #random.seed(240698) #for debugging, has been commented out
    
    #defining timestep
    dt = (t1/n_time)
    
    #initializing 225Rad and 225Ac arrays
    count_rad = numpy.zeros((n_time))
    count_act = numpy.zeros((n_time))
    
    #initializing array for total number of atoms.
    atoms = numpy.ones(N0)
    
    #decay probability within a timestep
    p_decay_rad = 1 - (numpy.exp(-dt/TAU_Ra))
    p_decay_act = 1 - (numpy.exp(-dt/TAU_Ac))
     
    # loop: for each timestep
    for time in range(n_time):
        #count the number of 225Rad (1) and 225Ac (2) atoms and store these 
        #in the appropriate time point in their respective array
        count_rad[time] = (atoms == 1).sum()
        count_act[time] = (atoms == 2).sum()
        # loop: for each atom
        for atom in range(N0):
            #check if it's Actinium
            if atoms[atom] == 2:
                #simulate random decay
                if p_decay_act >= random.random():
                    #set atom label to 221Fr (which we're not really counting)
                    atoms[atom] = 3
            #check if it's Radium
            if atoms[atom] == 1:
                #simulate random decay
                if p_decay_rad >= random.random():
                    #set atom label to actinium
                    atoms[atom] = 2

    #returns the 225Ra and 225Ac arrays 
    return count_rad, count_act

#returns the Differential Equations describing the decay of 225Ra and 225Ac    
def f((N_rad, N_act), t):
    dN_rad = -N_rad/TAU_Ra
    dN_act = -N_act/TAU_Ac - dN_rad
    return numpy.array((dN_rad, dN_act))

#Assigning initial values
N_rad, N_act = N0, 0  

#evaluating each method
n_analytic = analytic(N0, ts)
n_rad = monte_carlo_sim(N0, t1, n_time)[0]
n_act = monte_carlo_sim(N0, t1, n_time)[1]
n_scipy = scipy.integrate.odeint(f, (N_rad, N_act), ts)

#creating plot object
pyplot.figure(figsize=(9,6))

#plotting Atoms over time for 225Ra
pyplot.plot(ts, n_analytic, color = 'red', label = 'Radium - Analytical')
pyplot.plot(ts, n_rad, color = 'green', label = 'Radium - Monte Carlo')
pyplot.plot(ts, n_act, color = 'blue', label = 'Actinium - Monte Carlo')
pyplot.plot(ts, n_scipy[:,0], color = 'black', label = 'Radium - Scipy', linestyle = '--')
pyplot.plot(ts, n_scipy[:,1], color = 'cyan', label = 'Actinium -Scipy', linestyle = '--')

#plot formatting
pyplot.ylabel('Atom Count')
pyplot.xlabel('time [days]')
pyplot.title("Different methods for the Decay curves of a Radium population decaying into Actinium")
pyplot.legend()

#shows plot
pyplot.show()