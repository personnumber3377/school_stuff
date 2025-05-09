
from sympy import *

def s():
	eps = symbols("eps")
	A = Matrix([[1,1],[eps,0],[-eps,0]])
	the_thing = (A.T*A)
	eigenvals = the_thing.eigenvals()
	print(eigenvals)
	return


if __name__=="__main__":
	s()
	exit()
