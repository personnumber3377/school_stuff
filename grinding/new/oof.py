
from sympy import *

def print_repr(some_shit):
	print(str(some_shit).replace("exp", "e**"))
	return
'''

(-x*2*y)/(2*(x**2+y**2)*sqrt(y**2+x**2))

'''

def get_tangent_plane():
	# The thing is here the bullshit....
	x,y,z = Symbol('x'), Symbol('y'), Symbol('z')
	f = -z**2 + x*z + 3*y**2 - x*y + 2*x**2 - 10
	# Now do the thing...
	grad_f = [diff(f,var) for var in (x,y,z)]

	# Now do the thing..
	point = (1, 2, -1)
	
	grad_f = [thing.replace(x, point[0]).replace(y, point[1]).replace(z, point[2]) for thing in grad_f] # Just do the thing like this????
	# Now put the bullshit here:
	res = grad_f[0]*(x-point[0])+grad_f[1]*(y-point[1])+grad_f[2]*(z-point[2])
	print("Here is the result: "+str(res))
	return


def get_tangent_plane2():
	# The thing is here the bullshit....
	x,y,z = Symbol('x'), Symbol('y'), Symbol('z')
	f = (2*y - x + 3) / (3*y + 2*x+2) #  3*x**3-y**2 # -z**2 + x*z + 3*y**2 - x*y + 2*x**2 - 10
	# Now do the thing...
	grad_f = [diff(f,var) for var in (x,y,z)]

	# Now do the thing..
	# point = (1, 2, -1)
	point = (-3, 1, 0)
	
	grad_f = [thing.replace(x, point[0]).replace(y, point[1]).replace(z, point[2]) for thing in grad_f] # Just do the thing like this????
	
	print("Gradient point: "+str(grad_f))
	# Now put the bullshit here:
	res = f.subs(x, point[0]).subs(y, point[1]) + (grad_f[0]*(x-point[0])+grad_f[1]*(y-point[1])+grad_f[2]*(z-point[2]))


	print("Here is the result: "+str(res))
	
	print(diff(f,x).subs(x, -1).subs(y,1))
	print(diff(f,y).subs(x, -1).subs(y,1))

	return


def solve_problem():
	x,y,z = Symbol('x'), Symbol('y'), Symbol('z')
	# x0, y0 = Symbol("x0"), Symbol("y0")

	# Now do the thing...
	# f = x*E**(-2*y)

	f = cos(7*x*y)*E**(8*(x**2+y**2+z**2))
	res = [diff(f, var) for var in (x,y,z)]
	#print(res)
	#print(res)
	for thing in res:
		print_repr(thing)
	return

def solve_problem2():
	x,y = Symbol("x"), Symbol("y")
	vector = Matrix([2*x**3*y**2, -2*x**3*y**3,-2*x**4*y**3])
	res = vector.jacobian([x,y])
	print(res)
	return
if __name__=="__main__":
	# solve_problem()
	get_tangent_plane2()
	exit(0)

'''

Using linear approximation, determine the maximum absolute relative error for the function
f(x,y,z) = -(3*x**2*y**3)/sqrt(z)
at (3,2,2)
, assuming that the relative errors with respect to x
, y
 and z
 are at most 2.1
%, 0.5
% and 1.9
%, respectively. Give your answer as a percentage.

'''
