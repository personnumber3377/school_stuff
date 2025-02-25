from sympy import *

def arclength(f_x, f_y, t, t0, t1):
	# Return the thing..
	integral = integrate(sqrt((diff(f_x, t)**2)+(diff(f_y, t)**2)), (t, t0, t1))
	return integral


def solve():
	t = Symbol('t')
	x = Symbol('x')
	y = Symbol('y')
	f_x = sqrt(7)*(t**3)/3
	f_y = 2*(t**2)
	a = Symbol('a')
	b = Symbol('b')
	res = arclength(f_x, f_y, t, 1, 5)
	print("Result: "+str(res))
	return

if __name__=="__main__":
	solve()
	exit(0)
# -23*sqrt(23)/21 + 191*sqrt(191)/21
