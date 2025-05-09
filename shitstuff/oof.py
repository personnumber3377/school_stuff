
from sympy import *


def s():
	d = symbols("d")
	# Solve the shit...
	l = 505*(10**(-9)) # nanometers
	L = 1.81
	delta_y = 0.725*10**(-2)
	equation = Eq(delta_y, l*L/d)
	sol = solve(equation, d)
	print(sol)
	print(sol[0]*100)
	return

if __name__=="__main__":
	s()
	exit(0)
