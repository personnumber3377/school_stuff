
from sympy import *

def s():
	# Do the thing here...
	delta = symbols("delta")
	A = Matrix([[1,1],[0,1+2*delta]]) # The matrix
	# Diagonalize
	V, Lambda = A.diagonalize()
	# print(res)
	print("V: "+str(V))
	print("Lambda: "+str(Lambda))
	# Now calculate the condition number kappa:
	K = V.condition_number() # This here gives a symbolic result.
	print("K(V): "+str(K))
	return

if __name__=="__main__":
	s()
	exit(0)
