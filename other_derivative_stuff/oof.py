
from sympy import *



if __name__=="__main__":
	# Now do the shit...
	x, y = Symbol("x"), Symbol("y")
	# Now define the function...
	f = 1 - sqrt(y**2+4*x**2) # Define the shit...
	# Now calculate the stuff.
	diff_x = diff(f, x)
	diff_y = diff(f, y)
	# Now calculate the derivatives
	#print(diff_x.subs(x, 1).subs(y, 1))
	print(diff_x.subs(y, 0).subs(x, 0))

	#print(diff_y.subs(x, 1).subs(y, 1))
	#print(diff_y.subs(x, 0).subs(y, 0))
	exit(0)

'''
no
no
-4*sqrt(5)/5
-sqrt(5)/5
'''
