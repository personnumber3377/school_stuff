
from sympy import *
import math

def print_repr(expression):
	print(str(expression).replace("exp", "e**"))

def get_derivatives(f, variables): # Get's all of the derivatives both 1st, 2nd, third etc order..
	out = [f]
	# First get the first order, second order etc etc...
	f_cur = [f]
	for degree in range(len(variables)):
		f_new = []
		for function in f_cur:
			for var in variables:
				f_new.append(diff(function, var))
		out.extend(f_new)
		f_cur = f_new
	return out

if __name__=="__main__":
	x, y = Symbol("x"), Symbol("y") # Our variables...
	variables = [x, y]
	# f = x*E**(-x*y**2)
	f = y*E**(x*y**2)
	result = get_derivatives(f, variables)
	values = [1,-2]
	# result = [f] + result # Add the initial value
	#print("Derivatives: ")
	#print(result)
	print("Result: "+str(result))
	print("Length of result: "+str(len(result)))
	assert len(result) == 7
	for der in result:
		res = der
		for i, var in enumerate(variables):
			res = res.subs(variables[i], values[i])
		print_repr(res)
	
	exit(0)
