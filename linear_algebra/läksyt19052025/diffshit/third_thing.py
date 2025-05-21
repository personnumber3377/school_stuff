
from sympy import * # Import all the stuff from the thing...

def s():
	t = symbols("t")
	Q = 1/sqrt(2)*Matrix([[1,1],[1,-1]]) # Value of Q
	x_0 = Matrix([[1],[0]]) # x0 = [1,0]
	e_lambda_t = Matrix([[E**(4*t), 0], [0, E**(-2*t)]]) # We have the thing here...
	e_At = Q @ e_lambda_t @ Q.transpose()
	print(e_At)
	res = e_At @ x_0
	print(res) # Print out the result
	return

if __name__=="__main__":
	s()
	exit()
