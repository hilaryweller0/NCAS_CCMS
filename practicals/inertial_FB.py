# Numerical solution of the inertial osicllation equation using
# forward-backward time-stepping with Coriolis parameter f
# dudt = f*v
# dvdt = -f*u

import numpy as np      # External library for numerical calculations
import matplotlib.pyplot as plt   # Plotting library

# Setup parameters
f = 1e-4                # Coriolis parameter
nt = 12                 # Number of time steps
dt = 5000               # Time step in seconds
# Initial conditions (in meters or m/s)
x0 = 0.
y0 = 1e5
u0 = 10.
v0 = 0.
# Initialise velocity from initial conditions
u = u0
v = v0
# Store all locations for plotting and store initial locations
x = np.zeros(nt+1)
y = np.zeros(nt+1)
x[0] = x0
y[0] = y0

# Loop over all time-steps
for n in range(nt):
    u += dt*f*v
    v -= dt*f*u
    x[n+1] = x[n] + dt*u
    y[n+1] = y[n] + dt*v

# Analytic solution for the location as a function of time
times = np.linspace(0,nt*dt, nt+1)
xa = x0 + 1/f*(u0*np.sin(f*times) - v0*np.cos(f*times) + v0)
ya = y0 + 1/f*(u0*np.cos(f*times) + v0*np.sin(f*times) - u0)

# Plot the solution in comparison to the analytic solution
plt.plot(xa, ya, '-k+', label='analytic')
plt.plot(x, y, '-bo', label='forward-backward')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

