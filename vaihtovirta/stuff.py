
from sympy import *
# from math import pi
# from math import pi
import math
def s():
	f, t, dx = symbols("f t dx")
	#dx = 0.0003 # 0.03 cm in meters
	#f = 2000 # Hz
	x = sin(f*2*pi*t)*dx
	v = diff(x,t)
	# sol = solve(v, t)
	a = diff(v,t)
	sol = solve(a, t)
	print("Sol: "+str(sol))
	v_at_0 = v.subs(t,0)
	print(v_at_0)

	dx_val = 0.0003
	f_val = 2000
	B = 0.5
	l = 0.018
	sol2 = v_at_0*B*l
	sol2 = sol2.subs(dx, dx_val).subs(f,f_val).subs(pi, math.pi)
	print("Sol2: "+str(sol2))

	return


if __name__=="__main__":
	s()
	exit(0)

