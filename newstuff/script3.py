from sympy import *
from derivatives import *




def display_der(f):
	print(str(f).replace("log", "ln"))

def solve_thing():
	# Just do the thing.
	x, y, z = Symbol("x"), Symbol("y"), Symbol("z")
	f = 4*y**2 - x*y + y + 2*(x+2)*(-y+1)-x**2 # 3*x**2*y**3*z - 2*x**4*y**2*z
	f_x = diff(f, x)
	f_y = diff(f, y)

	print(f_x.subs(x, -1).subs(y, -1))
	print(f_y.subs(x, -1).subs(y, -1))

	#print(f_x.subs(x, 1).subs(y, 1))
	#print(f_y.subs(x, 1).subs(y, 1))
	#assert len(derivatives_stuff) == 4
	return

if __name__=="__main__":
	solve_thing()
	exit(0)

