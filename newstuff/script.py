from sympy import *
from derivatives import *






def solve_thing():
	# Just do the thing.
	x, y = Symbol("x"), Symbol("y")
	f = x*E**y+ln(x)*y
	derivatives_stuff = get_derivatives(f, [x,y])
	# We need to get rid of the first derivatives
	derivatives_stuff.pop(0)
	derivatives_stuff.pop(0)
	derivatives_stuff.pop(0)
	#print("Derivatives: "+str(derivatives_stuff))
	point = [6,6]
	for der in derivatives_stuff:
		print(der.subs(x, 6).subs(y,6))

	assert len(derivatives_stuff) == 4

if __name__=="__main__":
	solve_thing()
	exit(0)

