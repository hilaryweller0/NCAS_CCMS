import numpy as np                # External library for numerical calculations
import matplotlib.pyplot as plt   # Plotting library
%matplotlib auto                  # Makes plots show in a different window

def initialBell(x):
    "Initial conditions as a function of space, x"
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0.)

# Setup space, x, initial phi profile and Courant number
nx = 40; nt = 40        # number of points in space and time
c = 0.2                 # The Courant number
x = np.linspace(0.0, 1.0, nx+1) # From zero to one inclusive
phi = initialBell(x)    # Three time levels of the dependent variable, 
phiNew = phi.copy()     # phi
phiOld = phi.copy()

# derived or assumed quantities
u = 1.0; dx = 1./nx; dt = c*dx/u

# Plot the initial conditions
plt.plot(x, phi, 'k', label='initial conditions')
plt.legend(loc='best')
plt.ylabel(r'$\phi$')
plt.axhline(0, linestyle=':', color='black')
plt.pause(1)

# FTCS for the first time-step, looping over space
for j in range(1,nx):       # loops from 1 to nx-1
    phi[j] = phiOld[j] - 0.5*c*(phiOld[j+1] - phiOld[j-1])
# apply periodic boundary conditions
phi[0] = phiOld[0] - 0.5*c*(phiOld[1] - phiOld[nx-1])
phi[nx] = phi[0]

# Loop over remaining time-steps (nt-1) using CTCS
for n in range(1,nt):       # loop from 1 to nt-1
    for j in range(1,nx):   # loop over space from 1 to nx-1
        phiNew[j] = phiOld[j] - c*(phi[j+1] - phi[j-1])
    # apply periodic boundary conditions
    phiNew[0] = phiOld[0] - c*(phi[1] - phi[nx-1])
    phiNew[nx] = phiNew[0]
    # update phi for the next time-step
    phiOld = phi.copy()
    phi = phiNew.copy()
    # Replot
    plt.cla()
    plt.plot(x, initialBell(x - u*n*dt), 'k', label='analytic')
    plt.plot(x, phi, 'b', label='CTCS')
    plt.legend(loc='best')
    plt.ylabel(r'$\phi$')
    plt.axhline(0, linestyle=':', color='black')
    plt.pause(0.05)

plt.show() # To keep the plot showing at the end

