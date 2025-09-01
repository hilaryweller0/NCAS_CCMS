import numpy as np
from GaussQuad import *

def testGaussQuad():
   """Testing of GaussQuad function"""
   # GaussQuad should integrate a linear exactly
   def linFunc(x):
       return 4*x + 2
   # Integral(linFunc) between -1, 2 is 
   # (4*4/2 + 4) - (4/2 - 2) = 12
   Iexact = 12
   Iquad = GaussQuad(linFunc, -1,2, N=3)
   error = Iquad - Iexact
   print("Error integrating linear function ",
         Iquad - Iexact)
   
   # Error should reduce a factor of 4 when
   # integrating sin(x) with 4 or 8 intervals
   Iquad4 = GaussQuad(np.sin, 0, 1, N=4)
   Iquad8 = GaussQuad(np.sin, 0, 1, N=8)
   Iexact = -np.cos(1) + np.cos(0)
   print("Error integrating sin with 4 points",
         Iquad4 - Iexact)
   print("Error integrating sin with 8 points",
         Iquad8 - Iexact)
   print("Error reduction which should be 4 is",
         (Iquad4 - Iexact)/(Iquad8 - Iexact))