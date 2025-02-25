from sympy import *
from derivatives import *




def display_der(f):
	print(str(f).replace("log", "ln"))

def solve_thing():
	# Just do the thing.
	x, y, z = Symbol("x"), Symbol("y"), Symbol("z")
	f = x**(y*ln(z)) # x*E**y+ln(x)*y
	derivatives_stuff = get_derivatives(f, [x,y])
	# We need to get rid of the first derivatives
	derivatives_stuff = derivatives_stuff[:3] # Just remove the second and third order derivatives.
	#print("Derivatives: "+str(derivatives_stuff))
	# point = [6,6]
	
	# print("Derivatives: "+str(derivatives_stuff))
	print("Derivatives: ")
	for der in derivatives_stuff:
		display_der(der)
	for der in derivatives_stuff:
		print(der.subs(x, E).subs(y,2).subs(z,E))

	#assert len(derivatives_stuff) == 4

if __name__=="__main__":
	solve_thing()
	exit(0)

