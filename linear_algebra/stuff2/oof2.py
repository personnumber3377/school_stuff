
from sympy import *

def s():
	mat1 = Matrix([[1,0,2],[0,1,0],[2,0,1]])
	mat2 = Matrix([[1, -sqrt(2), 3], [0,-2,0], [3, sqrt(2), 1]])

	# Matrix one first.

	eigenvals_mat_1 = mat1.eigenvals()

	eigenvects_mat_1 = mat1.eigenvects()

	print(eigenvals_mat_1.__repr__())
	print(eigenvects_mat_1.__repr__())

	# Matrix two:

	eigenvals_mat_2 = mat2.eigenvals()

	eigenvects_mat_2 = mat2.eigenvects()

	print(eigenvals_mat_2)
	print(eigenvects_mat_2)

	# Print the results as latex for easier copy paste.
	print("First matrix:")
	print(latex(eigenvals_mat_1))
	print(latex(eigenvects_mat_1))

	print("Second matrix:")

	print(latex(eigenvals_mat_2))
	print(latex(eigenvects_mat_2))

	return


if __name__=="__main__":
	s()
	exit()
