# -*- coding: utf-8 -*-
from __future__ import division
import matplotlib.pyplot as pyplot
import matplotlib.colors
import numpy

USER = 'Giulio Starace'
USER_ID = 'dzgf42'

v = 2 # run speed in microns/second
r0 = (20, 40) #initial position
k = 0.2 #sensitivity of bacteria to gradient change

dt = 0.1 #timestep
ts = numpy.arange(0, 100, dt) #Array of times

def f((x, y)): return 4000-(x**2 + y**2) #returns the energy function
    
def random(r0): #performs the random walk, returns the x's and y's over time
    a = numpy.random.uniform(0, 2*numpy.pi) #random initial angle
    x, y = r0 #setting initial x and y values
    shift = numpy.full(10, 2000, dtype=float) #intialising shift register of energies
    history = numpy.zeros((len(ts), len(r0))) #initializing array of trajectories
    for i in range(len(ts)):
        history[i] = x, y #storing x and y values
        eNew = f((x, y)) #calculating current energy
        shift = numpy.append(shift, eNew) #appending energy to shift register
        shift = shift[-10:] #holding only the 10 most recent values
        de = shift[-1] - shift[0] #calculating the difference in energies
        t_half = 1 + k*de/dt #half life definition
        if t_half <= 0.1: #half life should never be <= 0.1 
            t_half = 0.1
        tau = t_half/numpy.log(2) #necessary for the tumble probability
        P_tumble = 1-(numpy.exp(-dt/tau)) #definition of tumble probability
        if P_tumble >= numpy.random.random(): #tumble condition
            a = numpy.random.uniform(0, 2*numpy.pi) #choose a random angle
        else: #continue running in same direction
            x, y = x+v*numpy.cos(a)*dt, y+v*numpy.sin(a)*dt
    return history

#the next 8 lines are necessary for plotting f(x, y)
x0, x1 = -40, 50 #defining bounds
y0, y1 = -40, 50
xs = numpy.arange(x0,x1,1) #generating x and y values over which to evaluate
ys = numpy.arange(y0,y1,1) #f(x, y)
dat=numpy.zeros((len(xs), len(ys))) #array to hold function values
for ix, x in enumerate(xs):
    for iy, y in enumerate(ys):
        dat[iy,ix]=f((x,y))

fig = pyplot.figure(figsize=(10,8)) #initializing plot figure
ax1, ax2, ax3 =  pyplot.subplot(221), pyplot.subplot(222), pyplot.subplot(212)

displacements1 = numpy.empty((20, len(ts)))
displacements2 = numpy.empty((20, len(ts)))

for i in range(20): #obtaining data for 20 individuals
    trajectory = random(r0) #x's and y's due to random walk
    simp_xs = [trajectory[0,0], trajectory[-1,0]] #creates the simplified traj.
    simp_ys = [trajectory[0,1], trajectory[-1,1]]
    #calculates displacements (necessary later for MSD)
    displacements1[i] = (trajectory[:, 0]**2 +trajectory[:, 1]**2)
    displacements2[i] = ((trajectory[:, 0]-20)**2 +(trajectory[:, 1]-40)**2)
    
    ax1.plot(trajectory[:, 0], trajectory[:, 1]) #plots Chemotaxis traj
    im0 = ax1.imshow(dat, extent=(x0, x1,y0, y1), origin='lower', cmap=matplotlib.cm.gray)
    
    ax2.plot(simp_xs, simp_ys, marker = ".") #plots simplified traj
    im1 = ax2.imshow(dat, extent=(x0, x1,y0, y1), origin='lower', cmap=matplotlib.cm.gray)   
    
MSD1 = numpy.average(displacements1, axis=0)
MSD2 = numpy.average(displacements2, axis=0)
ax3.plot(ts, MSD1, color = "r", label= "MSD from (0,0)")
ax3.plot(ts, MSD2, color = "b", label= "MSD from (20, 40)")

#formatting
fig.suptitle('Simulation of the Chemotaxis of 20 Bacterium for a given energy function f(x,y)', fontweight = 'bold')
ax2.set_ylim(ymin = -10, ymax=42)
ax2.set_xlim(xmin = -10, xmax=22)
fig.colorbar(im1, ax = ax2, orientation='vertical', label='$f(x,y)=4000-(x^2 +y^2)$', fraction=0.060, pad=0.1)
ax1.set_title("Bacterium Trajectories")
ax1.set_ylabel("y [microns]") #this label is shared for both ax1 and ax2
ax1.set_xlabel("x [microns]")
ax2.set_title("Simplified Trajectories")
ax2.set_xlabel("x [microns]")
ax1.set_aspect('auto')
ax2.set_aspect('auto')
ax3.set_title("Mean Square Displacement of the Bacterium from different origins")
ax3.set_xlabel("Time [s]")
ax3.set_ylabel(r"MSD [microns$^2]$")
ax3.legend()
pyplot.tight_layout(rect=[0, 0.03, 1, 0.95])
pyplot.show() #showing plot 

ANSWER1 = '''For low k, the probability of tumbling increases - the bacteria
are essentially completely ignorant of the energy field, and ultimately do not 
converge. For large k, the bacteria are more sensitive to the energy field, and
hence largely restrict their tumbling until very close to convergence.'''