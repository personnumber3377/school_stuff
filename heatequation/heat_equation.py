
from sympy import * # Import all the shit.


def get_heat_equation_coeff(f, var): # This returns the value for c when f_t == c*(f_xx + f_yy) where f_xx is the double x derivative and f_yy is the double y derivative and f_t is the time derivative.
	# var are assumed to be in the form [x,y,t]
	assert len(var) == 3 # Must be three variables.
	f_t = diff(f, var[2])
	f_xx = diff(diff(f, var[0]), var[0])
	f_yy = diff(diff(f, var[1]), var[1])
	# Now solve.
	sol = solve(f_t - c * (f_xx + f_yy), c)
	return sol

if __name__=="__main__":
	x,y,t,c = Symbol("x"), Symbol("y"), Symbol("t"), Symbol("c")
	u = 6*E**(-2*t)*sin(6*(y+x)) # Run the thing...
	diff_variables = [x, y, t]
	c = get_heat_equation_coeff(u, diff_variables)
	print("Value for c: "+str(c))
	exit()
