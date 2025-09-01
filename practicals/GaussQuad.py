def GaussQuad(f, a, b, N = 100):
   """Gaussian quadrature integration of
   function f, betweeen a and b.
   Parameters:
      f (callable): Function to integrate
      a, b (float): Integration limits
      N (default 100): Number of intervals
   Returns
      I (float): The integral"""
   I = 0.
   dx = (b-a)/N
   for i in range(N):
      x = a + (i+0.5)*dx
      I += dx*f(x)
   return I