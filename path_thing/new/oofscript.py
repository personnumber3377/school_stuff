
from sympy import *
from other_implementation import *
def find_max_min_with_constraint(f, variables, constraints):
	# Finds the maximums and minimums within the given constraint functions...
	# First generate the stuff.
	# Define the stuff:
	# for the constraints, add the stuff.
	constr_variables = [Symbol("l"+str(i)) for i in range(len(constraints))] # Generate the lambda values...
	# Now check that there are no constraint variables in the original function.
	# free_vars = f.free_symbols # Free symbols thing...
	assert not set(f.free_symbols) & set(constr_variables)
	# Now do the constraint stuff.
	constraint_stuff = 0
	for constr_var, constr in zip(constr_variables, constraints):
		constraint_stuff += (constr) * constr_var # Add the thing...
	# Now we have the constraint stuff. Add it to the original function to get L
	L = f + constraint_stuff
	print("Lagrange function: "+str(L))
	# Now get the derivatives.
	derivatives_variables = [diff(L,v) for v in variables] # Derivatives with respect to the normal variables
	
	derivatives_lambdas = [diff(L,l) for l in constr_variables] # Derivatives with respect to lambdas.
	# Now try to do the stuff.
	# Solve the derivatives.
	derivatives_all = derivatives_variables + derivatives_lambdas
	print("Derivatives: "+str(derivatives_all))

	assert len(derivatives_all) == len(variables) + len(constr_variables)
	# They are all equal to zero, so we can just pass them like so.
	all_vars = variables + constr_variables
	print("all_vars: "+str(all_vars))
	print("All derivatives: "+str(derivatives_all))
	sol = solve(derivatives_all, all_vars)
	# Now output the solution.
	print("Solution: "+str(sol))
	# print("Min or max value: "+str(f.subs(sol)))
	res = []
	
	min_thing = None
	max_thing = None
	
	max_res = None
	min_res = None
	print(sol)
	for s in sol: # Solution.
		# result = f.subs(s)
		result = f
		for i, x in enumerate(s[:len(variables)]):
			result = result.subs(variables[i], x)
		# Now check
		if not min_thing or result <= min_res:
			if result == min_res:
				print("Another solution thing: "+str(s))
				print("Previous: "+str(min_thing))
				print(min_res)
				# assert False
			min_thing = s
			min_res = result

		if not max_thing or result >= max_res:
			max_thing = s
			max_res = result

	print("Max critical point: "+str(max_thing))
	print("Min critical point: "+str(min_thing))
	print("Max value obtained: "+str(max_res))
	print("Min value obtained: "+str(min_res))

	return

def test():
	x,y,z = Symbol("x"), Symbol("y"), Symbol("z")
	constr = z**2+2*y**2+4*x**2-81
	f = 4*z+3*y+3*x
	find_with_constraints(f, [x,y,z], [constr])
	return

if __name__=="__main__":
	# test_constraints()
	test() # Run the thing...
	exit(0)

