
from sympy import *
from myhessian import *

def sol():
	x,y = Symbol("x"), Symbol("y")# , Symbol("z")
	g = 2*x**3+x**2*y+6*x**2-y # x**2 + 2*y**2+3*z**2+x*y+2*x*z+3*y*z-20*x
	# 
	g_xx = diff(diff(g,x),x) # Double x derivative
	g_yy = diff(diff(g,y),y) # Double y derivative
	g_xy = diff(diff(g,x),y)
	# Now try to compute the determinant thing...
	# det = g_xx*g_yy - (g_xy)**2
	# print("Determinant: "+str(det))
	# Max critical point: (1, -9, l0)
	# Min critical point: (-1, -3, l0)
	# 
	h = myhessian(g, [x,y]) # Get the hessian matrix.
	l = Symbol("l")
	#l1 = Symbol("l1")
	print(h)
	equation = (h[0][0] - l)*(h[1][1] - l) - h[0][1] * h[1][0]
	p0 = equation.subs(x, 1).subs(y,-9)
	p1 = equation.subs(x, -1).subs(y,-3)
	sol1 = solve(p0, [l])
	sol2 = solve(p1, [l])
	print(sol1)
	print(sol2)
	return 


if __name__=="__main__":
	sol()
	exit(0)
