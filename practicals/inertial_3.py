def inertialSteps(x0,y0,u0,v0,f,dt,nt,method):
    """Numerical solutions of the inertial
    oscillation equation.
    Parameters:
    x0, y0 (float): The starting point.
    u0, v0 (float): The initial velocity.
    f (float): The Coriolis parameter.
    dt (float): The time step.
    nt (int): The number of time steps.
    method (callable): The time stepping
        method taking artuments u, v, dtf.
    Returns:
    x, y (arrays): Location at each step."""
    # Declare and initialise location arrays
    x = np.zeros(nt+1);  y = np.zeros(nt+1)
    x[0] = x0;  y[0] = y0
    # Loop over all time steps
    for n in range(nt):
        # New velocity
        u,v = method(u0, v0, dt*f)
        # Average velocity over time step
        ubar = 0.5*(u0 + u)
        vbar = 0.5*(v0 + v)
        # New locations
        x[n+1] = x[n] + dt*ubar
        y[n+1] = y[n] + dt*vbar
        # Update u0 and v0 for next time step
        u0 = u
        v0 = v
    return x,y