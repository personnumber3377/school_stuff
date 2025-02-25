
from myhessian import * # From my hessian implementation...
from sympy import *

def evalf(f, x_val, y_val, x, y):
	return f.subs(x, x_val).subs(y, y_val)

def sol() -> None:
	# Solve function...
	x,y = Symbol('x'), Symbol('y')
	# Now do the thing...
	# critical_points = sp.solve([fx, fy], (x, y))

	f = -3*(y**2) - 2*x*y + 10*y + 3*(x**2) - 10*x # 2*(x**2) - 6*x*y - 6*(x**2)*y
	fx = diff(f,x)
	fy = diff(f,y)
	critical_points = solve([fx, fy], (x, y))
	print("Critical points: "+str(critical_points))
	diff2 = 0.1
	x_actual = 2
	y_actual = 1
	print(evalf(f, x_actual, y_actual, x, y))
	print(evalf(f, x_actual+diff2, y_actual, x, y))
	print(evalf(f, x_actual, y_actual+diff2, x, y))

	print(evalf(f, x_actual-diff2, y_actual, x, y))
	print(evalf(f, x_actual, y_actual-diff2, x, y))
	return
# -6*(2/3) - 2*sqrt(36*(-1)**2 + 36*(-1) + 9*(2/3)**2 - 6*(2/3) + 10) + 2
# -6*(2/3) + 2*sqrt(36*(-1)**2 + 36*(-1) + 9*(2/3)**2 - 6*(2/3) + 10) + 2
if __name__=="__main__":
	sol()
	exit(0)
