'''this module examines the projecticle motion of a spherical iron cannonball
launched in the presence of Earth's gravity and drag forces. The optimal launch
angle for range is then determined within +/- 5 degrees'''

from __future__ import division
import numpy
import scipy.integrate
import matplotlib.pyplot as pyplot

USER = 'Giulio Starace'
USER_ID = 'dzgf42'

#constants here
r = 0.15 #radius of cannonball in meters
rho_iron = 7874.00 #density of iron in kgm^-3
g = 9.81 #acc due to grav in ms^-2
kappa = 0.47 #drag coefficient of a sphere
rho_air = 1.23 #density of air in m^3
t1 = 25.00 #end time for our ODE integration in s
v0 = 125.00 #launch speed in ms^-1
n_panels = 400 #the number of panels to use

m = rho_iron * (4/3)*numpy.pi*r**3 #mass of cannon ball in kg
area = numpy.pi*r**2 #cross sectional area of cannon ball in m^2

#given cannonball x and y pos and vel at time t
#returns a four element numpy array of the cannonball x and y vel and acc
def f((x,y,vx,vy),t):
    #forces on cannonball
    Fx_grav = 0
    Fy_grav = -m*g
    Fx_drag = -kappa*rho_air*area*numpy.sqrt(vx**2 + vy**2)*vx
    Fy_drag = -kappa*rho_air*area*numpy.sqrt(vx**2 + vy**2)*vy
    #computing outputs
    d_x = vx 
    d_y = vy
    d_vx = Fx_drag/m
    d_vy = (Fy_drag + Fy_grav)/m
    return numpy.array((d_x, d_y, d_vx, d_vy))

#given an initial state array (x) and number of panels to use  
#returns numpy 2D numpy array of x, y, vx, vy at different times using Euler mthd 
def solve_euler(x, t1, n_panels):
    dt = t1/n_panels #determining dt
    history = numpy.zeros((n_panels, len(x))) #will allocate values in here
    for i in range(n_panels):
        history[i] = x
        #the t in f(x, t) is trivial so we put t=0 to emphasize this
        x = x + f(x, 0) * (dt) #euler method
            
    return history
        

pyplot.figure(figsize=(8,6))
timebase = numpy.arange(0, t1, t1/n_panels)

#process a trajectory to terminate it when it goes below y=0
def trim_trajectory(values):
    for i in range(len(values)-1):
        x0, y0, vx0, vy0 = values[i]
        x1, y1, vx1, vy1 = values[i+1]
        if y0 < 0: return values[:i]
    return values

proj_range = []
thetas = range(5, 90, 5) #angles to explore in degrees 
pyplot.subplot(211)

#calculates height and distance for each angle and stores it in a numpy array
for theta in thetas:
    #definition of vx and vy from trig
    vx, vy = v0*numpy.cos(numpy.radians(theta)), v0*numpy.sin(numpy.radians(theta))
    initial_conditions = (0, 0, vx, vy)
    
    values_scipy = scipy.integrate.odeint(f, initial_conditions, timebase)
    values_euler = solve_euler(initial_conditions, t1, n_panels)
    values_scipy = trim_trajectory(values_scipy)
    values_euler = trim_trajectory(values_euler)
    #calculating range for each angle
    x_first, y_first, vx_first, vy_first = values_scipy[0]
    x_final, y_final, vx_final, vy_final = values_scipy[-1]
    rnge = x_final-x_first
    proj_range.append(rnge)
 
    #plotting scipy and euler methods on same plot: height vs distance
    pyplot.plot(values_scipy[:,0], values_scipy[:,1], color = "gray", label = "Scipy Trajectories")
    pyplot.plot(values_euler[:,0], values_euler[:,1], color = "blue", linestyle = '--', label = "Euler Trajectories")
    pyplot.xlabel('Distance [meters]')
    pyplot.ylabel('Height [meters]')

#formatting plot with better spacing and labels
pyplot.subplot(211).set_ylim(ymin=-20)
pyplot.subplot(211).set_xlim(xmin=-10)
pyplot.legend(["SciPy", "Euler"])
pyplot.title("Trajectory of a Cannonball launched over different Angles under Gravity and Drag")

#plot range vs angles 
pyplot.subplot(212)
pyplot.plot(thetas, proj_range)
pyplot.ylabel('Range [meters]')
pyplot.xlabel('Launch Angle [degrees]')
pyplot.title("Cannonball Range as a function of Launch Angle")
pyplot.tight_layout() #fixing spacing issues between plots
pyplot.show()

ANSWER1 = '''From the plot, the angle from the horizontal for maximum range
appears to be approximately 40 degrees'''
ANSWER2 = '''The angle for maximum range decreases with increasing air density
as there would be a greater resistive force. In x, this would require a
greater vx. In y, this would relax the need for a greater vy as gliding would 
become easier. Both these lower theta as cos(theta)-->1 and sin(theta)-->0 as
theta-->0, for the range of angles considered.'''