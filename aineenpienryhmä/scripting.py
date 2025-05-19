
from sympy import *


def brackets():
	actual_x = symbols("x")
	x = actual_x
	L = symbols("L")

	phi = sqrt(2/L)*sin(pi*x/L)

	integral_stuff = x*phi**2
	# almost_inf = 1000000000000000
	result = integrate(integral_stuff, (x, 0, L))
	# print(result)
	result = simplify(result)
	
	print(result)
	return result

def brackets_squared():
	actual_x = symbols("x")
	x = actual_x**2
	L = symbols("L")

	phi = sqrt(2/L)*sin(pi*actual_x/L)

	integral_stuff = actual_x**2*phi**2

	# integral_stuff = actual_x**2*2/L*sin(pi*actual_x/L)**2
	print("integral_stuff : "+str(integral_stuff))
	# almost_inf = 1000000000000000
	result = integrate(integral_stuff, (actual_x, 0, L))
	print(result)
	result = simplify(result)
	return result

def keskihajonta(x_thing):
	print("Here is the bullshit: brackets(x_thing, x_thing): "+str(brackets()))
	return sqrt(brackets_squared() - brackets()**2)

def first_part(x, L, h_bar):
	# Now define phi here

	phi = sqrt(2/L)*sin(pi*x/L)

	integral_stuff = x*phi**2
	almost_inf = 1000000000000000
	result = integrate(integral_stuff, (x, 0, L))
	result = simplify(result)
	print(result)

	# Now calculate momentum

	momentum_stuff = phi*(-I*h_bar*diff(phi,x))

	# res2 = integrate(momentum_stuff, (x, -oo, oo))
	res2 = integrate(momentum_stuff, (x, 0, L))
	res2 = simplify(res2)
	print(res2)
	return

def s():
	x, L, h_bar = symbols("x L h_bar")

	# first_part(x, L, h_bar)

	keskihajonta_paikka = keskihajonta(x)
	keskihajonta_paikka = simplify(keskihajonta_paikka)
	keskihajonta_paikka = simplify(keskihajonta_paikka)
	print(keskihajonta_paikka)

	return

if __name__=="__main__":
	s()
	exit()
