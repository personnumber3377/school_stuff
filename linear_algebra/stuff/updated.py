
from sympy import *

def calculate(eps): # Calculates eigenvalues etc for the given value of epsilon
	print("="*100+"\n")
	print("Case when epsilon = "+str(eps))
	A = Matrix([[1,1],[eps,0],[-eps,0]])
	nullspc = A.nullspace()
	print("Nullspace: "+str(nullspc))
	# Calculate nullspace of the matrix first...
	the_thing = (A.T*A) # We just proved that the null space is the same as the null space of (A.T*A)
	eigenvals = the_thing.eigenvals() # Eigenvalues
	eigenvectors = the_thing.eigenvects() # Eigenvectors
	print(eigenvals)
	print(eigenvectors)
	print("="*100+"\n")
	return

def s():
	vals = [1, 10**(-6), 10**(-9)]
	for val in vals:
		calculate(val)
	return


if __name__=="__main__":
	s()
	exit()
