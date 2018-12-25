from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER = "Giulio Starace"
USER_ID = "dzgf42"

def f(x):
    '''computes cos(x). Can input/output either single or array of numbers'''
    return numpy.cos(x)
    
def g(x):
    '''Analytical derivative of f(x) w.r.t x'''
    return -numpy.sin(x)
    
def g_bdm(x, dx):
    '''Numerical derivative of f(x) using Backwards Difference Method'''
    return (f(x+dx)-f(x))/dx
    
#defining x values. 100 values equally spaced between -2pi and 2pi.
xs = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 100)

#evaluating derivatives
df_dx_small = g_bdm(xs, dx=1e-15)
df_dx_large = g_bdm(xs, dx=1e4)
df_dx_good = g_bdm(xs, dx=1e-4)

#analytical 
df_dx_analytical = g(xs)

#setting plot size
pyplot.figure(figsize=(8,4))

#creating plots
good =  pyplot.plot(xs, df_dx_good - df_dx_analytical, label="well chosen: dx = 1e-4")
small = pyplot.plot(xs, df_dx_small - df_dx_analytical, label="too small: dx = 1e-14")
large = pyplot.plot(xs, df_dx_large - df_dx_analytical, label="too large: dx = 1e4")

#labelling plots
pyplot.title("Error in derivative of f(x) with respect to x for different values of dx")
pyplot.legend(loc=3, prop={'size': 9})
pyplot.xlabel("x [radians]")
pyplot.ylabel("Error in Numerical Derivative")

#showing plots
pyplot.show()

ANSWER1 = "Accuracy is lost where dx is too small because it approaches division by 0, producing the erratic plot shown. Large dx suffers because it approaches a value of 0 for the entire derivative for every value, which is false."