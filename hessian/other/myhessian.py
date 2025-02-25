#!/bin/sh

# This file implements the calculating of a hessian with pythons symbolic calculation library sympy.

import sympy
import numpy as np



def generate_sequences(dimensions, max_n):
	current = [0] * dimensions  # Initialize the list to [0, 0, ..., 0]

	while True:
		# Yield the current sequence
		yield current.copy()

		# Increment the indices like counting
		for i in range(dimensions):
			current[i] += 1
			if current[i] < max_n:
				break  # Stop if within bounds
			current[i] = 0  # Reset current index and carry to the next
		else:
			# If we exit the for loop without breaking, we are done
			return


import copy

def set_element(lst, indices, value):
	current = lst
	for i in indices[:-1]:  # Navigate through the list of lists
		current = current[i]
	current[indices[-1]] = value  # Set the value at the final index

def myhessian(function, variables): # Calculate the hessian.
	assert len(variables) >= 2 # Should have two or more variables to take the hessian.
	output_matrix = np.zeros([len(variables) for _ in variables]) # Should generate a hypercube matrix.
	#print(output_matrix)
	output_matrix = output_matrix.tolist() # Convert to python list, because otherwise we can not put symbolic stuff.

	variable_indexes = generate_sequences(2, len(variables))


	for seq in variable_indexes:
		# Now the variable indexes are in seq.
		cur_thing = output_matrix
		res = copy.deepcopy(function)
		for ind in seq:
			cur_thing = cur_thing[ind] # Get the thing
			res = sympy.diff(res, variables[ind]) # Just do the shit.
			#print("Result: "+str(res))
		# Now assign the thing.
		# cur_thing = res # Assign the element. This works, because this is a reference to the list, not the actual value...
		set_element(output_matrix, seq, res)
	#print(output_matrix)
	return output_matrix

def test_basic():
	x, y, z, t = sympy.Symbol("x"), sympy.Symbol("y"), sympy.Symbol("z"), sympy.Symbol("t")
	variables = [x,y,z]
	# f = x**2 + y**2
	f = x**2 + y**2 + z**2 + 2*t*(x*y + y*z + x*z) # Here is the function
	res = myhessian(f, variables)
	print("Result: "+str(res))
	expected = sympy.hessian(f, (x, y, z)) # Run the thing
	print("Reference result: "+str(expected))
	point = {x: 0, y: 0, z: 0}

	# Substitute the point into the Hessian matrix
	H_evaluated = expected.subs(point)

	# Display the evaluated Hessian
	print(sympy.Matrix(H_evaluated))
	return

def run_tests(): # This function runs the tests of the program.
	test_basic()
	return


if __name__=="__main__":

	# Example usage:

	run_tests()
	exit(0)

