# -*- coding: utf-8 -*- <----why does this keep showing up in my code?
from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER = 'Giulio Starace'
USER_ID = 'dzgf42'

def f(z): return z**4 - 1 #the function that needs root finding
    
def analytical(z): return 4*(z**3) #f'(z), necessary for NR

def NR(z): #uses Newton Raphson to compute roots of an equation
    MAX_ITER = 30
    for step in range(MAX_ITER):
        z = z - f(z)/analytical(z) #NR algorithm
        if abs(f(z)) < 0.001: #break when very close to finding the root
            break
    arg = numpy.angle(z)
    if numpy.pi - abs(arg) < 1e-2: #pi and -pi have same root
        arg = numpy.pi #approximate to pi when very close
    return arg, step
      
x0, x1 = -2, 2 #defining x and y ranges to "test" as roots, will be plotted
y0, y1 = -2, 2
real = numpy.arange(x0,x1,4/300)
imaginary = numpy.arange(y0,y1,4/300)

args=numpy.zeros((len(real), len(imaginary))) #initializing arrays to hold
steps =numpy.zeros((len(real), len(imaginary)))#function values
for ix, x in enumerate(real):
    for iy, y in enumerate(imaginary):
        z = x + 1j*y
        args[iy,ix], steps[iy,ix]=NR(z) #populating these arrays
        
fig = pyplot.figure(figsize=(10,8)) #creating plot and subplots
ax1, ax2, ax3, ax4 = pyplot.subplot(221), pyplot.subplot(222), \
pyplot.subplot(223), pyplot.subplot(224)

im1 = ax1.imshow(args, extent=(x0, x1,y0, y1)) #plotting
fig.colorbar(im1, ax=ax1, orientation='vertical', label='$arg(z)$')
im2 = ax2.imshow(steps, extent=(x0, x1,y0, y1))
fig.colorbar(im2, ax=ax2, orientation='vertical', label='Iterations')


#repeating the process at a more zoomed in level
x0, x1 = 0.1, 0.3 #defining zoomed bounds
y0, y1 = 0.1, 0.3
zoomreal = numpy.arange(x0,x1,0.2/300) 
zoomimaginary = numpy.arange(y0,y1,0.2/300)

zoomargs=numpy.zeros((len(zoomreal), len(zoomimaginary)))
zoomsteps =numpy.zeros((len(zoomreal), len(zoomimaginary)))
for ix, x in enumerate(zoomreal):
    for iy, y in enumerate(zoomimaginary):
        z = x + 1j*y
        zoomargs[iy,ix], zoomsteps[iy,ix]=NR(z)

im3 = ax3.imshow(zoomargs, extent=(x0, x1,y0, y1), origin = "middle") #plotting
fig.colorbar(im3, ax=ax3, orientation='vertical', label='$arg(z)$')
im4 = ax4.imshow(zoomsteps, extent=(x0, x1,y0, y1), origin = "middle")
fig.colorbar(im4, ax=ax4, orientation='vertical', label='Iterations')

#labeling
fig.suptitle('Application of the Newton-Raphson method for finding the roots of\
 a complex function', fontweight = 'bold')

ax1.set_title(r"Roots of $z^4 - 1$")
ax1.set_xlabel("Re(z)")
ax1.set_ylabel("Im(z)")

ax2.set_title("Convergence time of NR")
ax2.set_xlabel("Re(z)")
ax2.set_ylabel("Im(z)")

ax3.set_title("Roots - Zoomed in")
ax3.set_xlabel("Re(z)")
ax3.set_ylabel("Im(z)")

ax4.set_title("Convergence Time - Zoomed in")
ax4.set_xlabel("Re(z)")
ax4.set_ylabel("Im(z)")

#formatting
pyplot.tight_layout(rect=[0, 0.03, 1, 0.95])
pyplot.show()

ANSWER1 = '''The diagrams demonstrate chaotic behaviour given the areas of 
high colour contrast, indicating the high sensitivity to initial conditions. 
Furthermore, we see that the system is deterministic given that the same roots
are produced each time and that there is no randomness involved. The images
in the diagram are said to be fractal in nature due to the self similarity which
occurs throughout the patterns produced. This is highlighted by the zoomed in 
plots on the second row. Essentially, reguardless of scale, the pattern remains
the same.'''