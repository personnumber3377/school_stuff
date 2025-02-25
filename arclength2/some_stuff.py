#!/bin/python3

# This program here just implements a homework assignment I was given in university.

# The question is this: "Consider the curve r(t)=(t8,t8,t64). Determine the exact value of the cosine of the angle between the tangent vector r′(1) and unit vector k of the given curve. For square root, write e.g. sqrt(17)."

from sympy import * # Namespace pollution, but idc


def cos_of_angle_between_vectors(A, B):
	dot_product = A.dot(B)  # Compute the dot product
	norm_A = sqrt(A.dot(A))  # Compute the magnitude of A
	norm_B = sqrt(B.dot(B))  # Compute the magnitude of B

	cos_theta = dot_product / (norm_A * norm_B)  # Compute cos(θ)
	#theta = acos(cos_theta)  # Compute θ in radians
	return cos_theta
	#return theta.simplify()  # Return simplified symbolic result



def tangent_vector(vector: Matrix, variable: Symbol) -> Matrix: # This returns the tangent vector (aka. 1 x n matrix) of the parametric curve.
	out = Matrix([diff(elem, variable) for elem in vector]) # Should output the tangent vector thing.
	return out

def solve():
	# solve the problem
	# Find the tangent vector r'(1) and its norm ||r'(1)||.
	t = Symbol('t') # Here is the thing...
	graph = Matrix([t**8, t**8, t**64]) # This is the bullshit thing...
	v_t = tangent_vector(graph, t) # Just differentiate with respect to "t".
	vector = v_t.subs(t, 1) # Set t = 1 to get the vector thing...
	print("Here is the vector: "+str(vector))
	# Calculate the norm of the vector:
	# print("Here is the first element: "+str(vector[0]))
	norm_of_vector = sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2) # Should return the precise value.
	print("Norm of the thing: "+str(norm_of_vector))
	k = Matrix([0,0,1])
	cos_of_angle = cos_of_angle_between_vectors(vector, k)
	print("Cosine of the angle: "+str(cos_of_angle))
	# Now calculate the angle
	angle = acos(cos_of_angle)
	print("Here is the angle: "+str(angle))
	# Now calculate angle between the vectors.
	return

if __name__=="__main__":
	# Main stuff here.
	solve()
	exit(0)
