import matplotlib.pyplot as pyplot
import matplotlib.colors
import numpy

USER = 'Giulio Starace'
USER_ID = 'dzgf42'

#computes the value of f(x, y) at given x and y
def f((x, y)):
    return ((1-x)**2+100*(y-x**2)**2)

#computes the gradient of f(x, y) at given x and y
def grad((x, y)):
    df_dx = 2*(200*x**3 - 200*x*y+x-1)
    df_dy = 200*(y-x**2)
    grad = numpy.array((df_dx, df_dy))
    return grad

#Use the gradient descent techniqe to minimise the function 'f' from r
def gradient_descent(r0, gamma):
    r = r0
    n_steps = 20000 #step number good compromise between accuracy & efficiency
    history = numpy.empty((n_steps, len(r0))) #initializing trajectory array
    for i in range(n_steps):
        history[i] = r
        r += -gamma*grad(r)
    return history #returns trajectory taken by Gradient Descent
        
# Define bounds 
x0, x1 = -0.2, 1.2
y0, y1 = -0.2, 1.2

#explore 1000 points in x and y
N_POINTS=1000
dx=(x1-x0)/N_POINTS
dy=(y1-y0)/N_POINTS 

#generate x and y values
xs=numpy.arange(x0,x1,dx)
ys=numpy.arange(y0,y1,dy)

#array to hold function values
dat=numpy.zeros((len(xs), len(ys))) 
    
for ix, x in enumerate(xs):
    for iy, y in enumerate(ys):
        dat[iy,ix]=f((x,y))

#obtaining the x and y values which minimize the function
trajectory = gradient_descent((1, 0.2), 0.0018)
xmin, ymin = trajectory[-1]

ANSWER1 = '''For too large gamma (> 0.0018), the GD trajectories oscillate 
sporadically and never settle into the minima valley within the for loop. For 
too small gamma (< 0.0012), the GD trajectories stop too early and don't reach 
the global minimum. For the right gamma values (0.0012 <= x <= 0.0018), the GD 
trajectories follow the valley all the way to the global minimum'''

ANSWER2 = '''Minimum (i.e. 0) occurs at (%.2f, %.2f)''' % (xmin, ymin)

#creating plot figure
pyplot.figure(figsize=(8,8))
# Show a greyscale colourmap of the data
im = pyplot.imshow(dat, extent=(x0, x1,y0, y1), origin='lower', 
cmap=matplotlib.cm.gray, norm=matplotlib.colors.LogNorm(vmin=0.01, vmax=200))

#plotting (and labeling) the trajectories of GD with different gamma values
labels = (r"$\gamma$ too small", r"$\gamma$ too large", r"$\gamma$ appropriate")
colors = ("blue", "red", "green")
gammas = (0.000001, 0.003, 0.0018)
for i in range(len(gammas)): 
    pyplot.plot(gradient_descent((1, 0.2), gammas[i])[:,0], gradient_descent((1, 0.2), gammas[i])[:,1], color = colors[i], label = labels[i])

#further labels
pyplot.title("Minimizing Rosenbrock's Banana Function using Gradient Descent")
pyplot.legend()
pyplot.xlabel('x')
pyplot.ylabel('y')
#colorbar tells maps f(x, y) value to greyscale shade 
pyplot.colorbar(im, orientation='vertical', label='$f(x,y)$', fraction=0.046, pad=0.04)
pyplot.tight_layout() #further formatting
pyplot.show()     