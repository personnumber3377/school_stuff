
from sympy import * # Import the sympy library and all the associated shit.

def relative_error(f, variables, point, relative_errors):
    """
    Compute the relative error of a function given relative errors in variables.

    :param f: The function (SymPy expression)
    :param variables: List of variables (SymPy symbols)
    :param point: Tuple of values (x0, y0, z0, ...)
    :param relative_errors: List of relative errors in percentage for each variable
    :return: The maximum absolute relative error as a percentage
    """
    # Compute the gradient of f
    grad_f = [diff(f, var) for var in variables]

    # Evaluate the gradient at the given point
    grad_values = [grad_f[i].subs(dict(zip(variables, point))) for i in range(len(variables))]

    # Compute the absolute relative error sum
    f_val = f.subs(dict(zip(variables, point)))
    print("f_val == "+str(f_val))
    rel_error_sum = sum(abs(grad_values[i]) * (relative_errors[i] / 100) for i in range(len(variables)))

    rel_error_sum = rel_error_sum / f_val

    # Return result as a percentage
    return rel_error_sum * 100 # * 100


def test_errors() -> None: # This is just a test function for the calculation of errors...
	#x,y,z = Symbol('x'), Symbol('y'), Symbol('z')
	#f = -(3*x**2*y**3) / sqrt(z) # Sample function.
	t, p = Symbol('t'), Symbol('p')
	n = 2.0
	R = 8.31447
	f = n*R*t/p
	evaluation_point = (319.4, 221.0) # Some point where we evaluate the error stuff...
	# max_rel_errors = [0.4/319.4*100, 0.04/221.0*100] # The relative errors respectively. (max_rel_err_x, max_rel_err_y ...)
	
	max_rel_errors = [0.4*100, 0.04*100]
	# rel_err = relative_error(f, [x,y,z], evaluation_point, max_rel_errors) # Get the result.
	rel_err = relative_error(f, [t,p], evaluation_point, max_rel_errors) # Get the result.
	print(rel_err)
	return


if __name__=="__main__":
	test_errors()
	exit(0)


