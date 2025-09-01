#Numerical solution of inertial oscillations
#with Coriolis parameter f.
# dudt = f*v, dvdt = -f*u

import numpy as np
import matplotlib.pyplot as plt

def inertial_FB(u, v, dtf):
    """Numerical solution of the inertial
    oscillation equation using forward-
    backward differencing for one time step.
    
    Parameters:
    u,v (float): Speeds in x and y directions 
         at the start of the time step.
    dtf: The product of the time step, dt, and
         the Coriolis parameter, f.
    
    Returns:
    u, v (float): The speeds at the end of the
         time step."""
    
    u += dtf*v
    v -= dtf*u
    return u,v