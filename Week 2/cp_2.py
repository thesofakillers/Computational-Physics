from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER = "Giulio Starace"
USER_ID = "dzgf42"

#returns x^2sin(x)
def f(x):
    return (x**2)*(numpy.sin(x))

#returns the integral of f(x), i.e 2xsin(x) -(x^2-2)cos(x)     
def g(x):
    return ((2*x*numpy.sin(x))-((x**2)-2)*numpy.cos(x))
    
#computes the definite integral of f(x) numerically using Simpson's Rule
#given limits and number of panels
def integrate_numeric(x0, x1, n_panels):
    panel_width = (x1-x0)/ n_panels
    area = 0
    
    #loop to apply simpsons rule formula to each panel
    for i in range (n_panels): 
        #find the left edge of this panel
        a = x0 + i*panel_width
        #find the right edge of this panel
        b = x0 + (i+1)*(panel_width)
        #find the middle of this panel
        m=(a+b)/2
        
        area += ((b-a)/6)*(f(a) + 4*f(m) +f(b))
    return area

#returns definite integral of f(x) analytically 
def integrate_analytic(x0, x1):
    y0 = g(x0)
    y1 = g(x1)
    return y1-y0
    

# range of panel sizes
PANEL_COUNTS = [4, 8, 1, 32, 64, 128, 256, 512, 1024]

#Bounds to integrate
X0, X1 = 0, 2

#Evaluate error for various panel counts
y_data =[]
ref = integrate_analytic(X0, X1)

for n in PANEL_COUNTS:
    s = integrate_numeric(0, 2, n)
    error = abs((s-ref)/ref)
    y_data.append(error)
    
pyplot.figure(figsize=(6,6))
pyplot.loglog()
#scatter plot of data points
pyplot.scatter(PANEL_COUNTS, y_data)
pyplot.xlabel("Number of Panels used")
pyplot.ylabel("Percentage Error in Numerical Method")
pyplot.title("Decreasing error in Simpson's Rule with increasing Panels")
pyplot.show()
#lines above create loglog plot of error vs number of panels

ANSWER1 = '''Increasing panel number increases the numerical accuracy because it decreases panel size. Smaller panels are preferred as they approach infinitesimal dimensions which are necessary for integration, which is a continuous, not discrete, process.'''
ANSWER2 = '''If trapezium rule had been used, increasing panel count would increase accuracy for the same reason it would when applying Simpson's Rule. However, this would be less accurate than Simpson's Rule with the equivalent amount of panels, since Trapezium Rule only contains first derivative (linear) information, compared to the inclusion of the 2nd derivative /quadratic) information in Simpson's Rule. '''