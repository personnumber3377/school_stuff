
from sympy import *

def sol():
	l,r1,r2,eps0 = symbols("l r1 r2 eps0")
	
	l = (15*10**(-9))/1 # 15 nanocoulombs per meters
	r2 = 0.025 # in meters 2.5cm
	eps0 = 8.8541878188*10**(-12) # Epsilon zero vaccuum permitivity.
	
	eq = Eq(175, l/(2*pi*eps0)*ln(r1/r2))
	print(eq)
	s = solve(eq,r1)
	print(s)

	

	return

if __name__=="__main__":
	sol()
	exit(0)
