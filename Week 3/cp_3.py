from __future__ import division

import numpy
import matplotlib.pyplot as pyplot

USER = 'Giulio Starace'
USER_ID = 'dzgf42'

T_HALF = 20.8 #halflife in hours
TAU = T_HALF/(numpy.log(2)) #Tau constant from Radioactive Decay
N0 = 1500 #Initial Number of Nuclei
T1 = 60 #integrate over time range 0 <= t < T1
N_PANELS = 15 #number of panels to divide the time range into

# returns the decay rate for n atoms in atoms per hour
def f(n):
    return -n/TAU
  

# returns numpy array of Atom counts at specified times using analytical sol'n   
def analytic(n0, ts):
    return n0 * numpy.exp(-ts/TAU)
    
# solves f(n) numerically using Euler's method
def solve_euler(n0, dt, n_panels):
    #Initialize simulation parameters
    n = n0
    #make an array to hold the counts at each time point 
    n_t = numpy.zeros((n_panels)) 
    #integrate each panel
    for i in range(n_panels):
        #assigning values to the array elements
        n_t[i] = n
        #calculate next timestep
        n = n + f(n)*dt #euler timestep involving f(n)
        
    return n_t

#solves f(n) numerically using Heun's Method
def solve_heun(n0, dt, n_panels):
    #initializing simulation parameters
    n = n0
    #make an array to hold the counts at each time point 
    n_t = numpy.zeros((n_panels)) 
    #integrate each panel
    for i in range(n_panels):
        k0 = f(n) 
        k1 = f(n + k0*dt)
        #assigning values to the array elements
        n_t[i] = n
        #calculate next timestep
        n = n + (dt/2)*(k0 + k1) #euler timestep involving f(n)
        
    return n_t
    
#width of a panel
dt = T1/N_PANELS

# Array of times used for plotting & analytical solution
ts = numpy.arange(0, T1, dt)

#Evaluation of various methods
n_analytic = analytic(N0, ts)
n_euler = solve_euler(N0, dt, N_PANELS)
n_heun = solve_heun(N0, dt, N_PANELS)

#Plotting Section of code
pyplot.figure()

#top plot: count vs time for methods
pyplot.subplot(211) 
pyplot.plot(ts, n_analytic, color = 'grey', label = 'Analytic')
pyplot.plot(ts, n_euler, color = 'red', label = "Euler's Method")
pyplot.plot(ts, n_heun, color = 'blue', linestyle = '--', label = "Heun's Method")
pyplot.ylabel('Atom Count')
pyplot.title("Iodene-133 Decay curves calculated through different methods")
pyplot.legend(prop={'size': 8})

#bottom plot: error vs time for numerics
pyplot.subplot(212) 
pyplot.semilogy() #make y-axis log
err_euler = abs(n_euler-n_analytic)/n_analytic
err_heun = abs(n_heun-n_analytic)/n_analytic
pyplot.plot(ts, err_euler, color = 'red', label = "Euler's Method")
pyplot.plot(ts, err_heun, color = 'blue', label = "Heun's Method")
pyplot.xlabel('time [hours]') #this label applies to both plots
pyplot.ylabel('Absolute Relative Error')
pyplot.legend(loc = 4, prop={'size': 8})

pyplot.show()

ANSWER1 = '''Heun's Method is more accurate than Euler's Method because it manages to use trapezium's rather than rectangles to integrate (using Euler's method along the way). This is achieved by the usage of more function evaluations: while Euler's method only predicts, Heun's Method predicts (using Euler) and then corrects this prediction accordingly, improving accuracy.'''