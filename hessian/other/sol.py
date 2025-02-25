
from myhessian import * # From my hessian implementation...
from sympy import *


def sol() -> None:
	# Solve function...
	x,y = Symbol('x'), Symbol('y')
	# Now do the thing...
	# critical_points = sp.solve([fx, fy], (x, y))

	f = 2*(x**2) - 6*x*y - 6*(x**2)*y
	fx = diff(f,x)
	fy = diff(f,y)
	critical_points = solve([fx, fy], (x, y))
	print("Should be zero 1: "+str(fx.subs(x, -1).subs(y, 2/3)))
	print("Should be zero 2: "+str(fy.subs(x, -1).subs(y, 2/3)))
	h = myhessian(f, [x,y]) # Calculate the hessian.
	print("Critical points: "+str(critical_points))
	print("Hessian matrix: "+str(h))
	h = Matrix(h)
	print("Eigenvals: "+str())
	eig_vals = h.eigenvals().keys()
	# Now substitute.
	eig_vals = list(eig_vals)
	# Now try to substitute the bullshit maybe????
	for val in eig_vals:
		print(val)
		print(val.subs(x, -1).subs(y,2/3))
	return
# -6*(2/3) - 2*sqrt(36*(-1)**2 + 36*(-1) + 9*(2/3)**2 - 6*(2/3) + 10) + 2
# -6*(2/3) + 2*sqrt(36*(-1)**2 + 36*(-1) + 9*(2/3)**2 - 6*(2/3) + 10) + 2
if __name__=="__main__":
	sol()
	exit(0)
