def errorVdt():
   """Variation of error with time step"""
   f = 1e-4   # Coriolis parameter
   endTime = 12*5000
   # Range of number of time steps and dts
   nts = [12,24,48,96,192]
   dts = np.zeros(len(nts))
   # Initial conditions
   x0 = 0.; y0 = 1; u0 = 1e-4; v0 = 0.
   # Final analytic solution
   xa = x0 + 1/f*(u0*np.sin(f*endTime)
             - v0*np.cos(f*endTime) + v0)
   ya = y0 + 1/f*(u0*np.cos(f*endTime)
             + v0*np.sin(f*endTime) - u0)
   methods = [inertial_FB, inertial_CN]
   tags = ["FB", "CN"]
   errs =np.zeros([len(methods),len(nts)])
   # Errors for each method and time step
   for im in range(len(methods)):
      for n in range(len(nts)):
         nt = nts[n]; dts[n] = endTime/nt
         x,y = inertialSteps(x0,y0,u0,v0,
                f,dts[n],nt,methods[im])
         errs[im,n] = ((x[-1]-xa)**2
                  + (y[-1]-ya)**2)**.5
      # Plot for this method
      plt.loglog(dts,errs[im],label=tags[im])
   plt.legend()
   plt.savefig('plots/inertialErrorVdt.pdf')