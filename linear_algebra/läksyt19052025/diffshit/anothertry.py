
from sympy import *


def s():
	# Solve the thing
	P = Matrix([[1,1],[1,0]]) # The thing
	J = Matrix([[2,1],[0,2]])
	x_0 = Matrix([[1],[0]])
	A_actual = Matrix([[3,-1],[1,1]])
	# Now do the thing...
	A_res = P @ J @ P.inv()
	print(A_res)
	# This should equal the given matrix
	assert A_res == A_actual
	# Now do the computation stuff...

	t = symbols("t") # Symbol

	# Now calculate e^(At)
	thing_matrix = Matrix([[1, t], [0,1]])
	e_At = P @ (E**(2*t) * thing_matrix) @ P.inv()

	print(e_At)

	# Now multiply with the initial condition x(0) = [1, 0] and it should give us the final result.
	res = e_At @ x_0
	print(res)
	return

if __name__=="__main__":
	s()
	exit(0)
