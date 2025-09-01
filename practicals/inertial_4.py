def inertial_CN(u, v, dtf):
    """Numerical solution of the inertial
    oscillation equation using Crank-
    Nicolson for one time step.
    
    Parameters:
    u,v (float): Speeds in x and y directions 
         at the start of the time step.
    dtf: The product of the time step, dt, and
         the Coriolis parameter, f.
    
    Returns:
    u, v (float): The speeds at the end of the
         time step."""
    
    uNew = (u + dtf*(v - dtf/4*u)) \
            /(1 + dtf**2/4)
    vNew = (v - dtf*(u + dtf/4*v)) \
            /(1 + dtf**2/4)
    return uNew,vNew