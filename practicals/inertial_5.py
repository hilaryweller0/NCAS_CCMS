#Compare forward-backward and Crank-
#Nicolson for intertial oscillations
def compareSolutions():
    # Parameters
    f = 1e-4   # Coriolis parameter
    nt = 12    # Number of time steps
    dt = 5000  # Time step in seconds
    # Initial conditions
    x0 = 0.; y0 = 1e5; u0 = 10.; v0 = 0.
    
    # FB solution
    xFB, yFB = inertialSteps(x0,y0,u0,v0,f,
                           dt,nt,inertial_FB)
    # CN solution
    xCN, yCN = inertialSteps(x0,y0,u0,v0,f,
                           dt,nt,inertial_CN)
    # Times
    times = np.linspace(0,nt*dt, nt+1)
    # Analytic solution
    xa = x0 + 1/f*(u0*np.sin(f*times)
                   - v0*np.cos(f*times) + v0)
    ya = y0 + 1/f*(u0*np.cos(f*times)
                   + v0*np.sin(f*times) - u0)
    # Plots
    plt.plot(xa, ya, '-k+', label='analytic')
    plt.plot(xFB, yFB, '-bo', label='FB')
    plt.plot(xCN, yCN, '-rx', label='CN')
    plt.legend()