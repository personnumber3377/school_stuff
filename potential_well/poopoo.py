
from sympy import *
import math

def s():
	#
	n = 1
	x = symbols("x")
	L = 0.24 * 10**(-9) # 0.24 nanometers
	# 0.0336 nm…0.2064 nm
	a = 0.0336 * 10**(-9)
	b = 0.2064 * 10**(-9)
	P = integrate(2/L*sin(n*math.pi*x/L)**2, (x,a,b))
	print(P)
	return

if __name__=="__main__":
	s()
	exit(0)
