
from sympy import *

def print_repr(some_shit):
	print(str(some_shit).replace("exp", "e**"))
	return
'''

(-x*2*y)/(2*(x**2+y**2)*sqrt(y**2+x**2))

'''


def solve_problem():
	x,y = Symbol('x'), Symbol('y')
	# x0, y0 = Symbol("x0"), Symbol("y0")
	x0,y0 = 1,2
	# Now do the thing...
	f = x*E**(-2*y)

	f_initial = f.subs("x", x0).subs("y", y0)
	f_x = diff(f,x)
	f_y = diff(f,y)
	f_xx = diff(f_x,x)
	f_yy = diff(f_y,y)
	f_xy = diff(f_x,y)

	f_xi = f_x.subs("x", x0).subs("y", y0)
	f_xxi = f_xx.subs("x", x0).subs("y", y0)

	f_yi = f_y.subs("x", x0).subs("y", y0)
	f_yyi = f_yy.subs("x", x0).subs("y", y0)

	f_xyi = f_xy.subs("x", x0).subs("y", y0)

	second_deg_taylor = f_initial+f_xi*(x-x0)+f_yi*(y-y0)+1/2*(f_xxi*(x-x0)**2+2*f_xyi*(x-x0)*(y-y0)+f_yyi*(y-y0)**2)
	print(str(second_deg_taylor))
	print_repr(second_deg_taylor)
	return

def solve_problem2():
	x,y = Symbol("x"), Symbol("y")
	vector = Matrix([2*x**3*y**2, -2*x**3*y**3,-2*x**4*y**3])
	res = vector.jacobian([x,y])
	print(res)
	return
if __name__=="__main__":
	solve_problem2()
	exit(0)
