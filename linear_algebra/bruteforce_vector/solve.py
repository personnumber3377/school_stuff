
from sympy import *
import random

MAX_INTEGER_MAGNITUDE = 10 # Use low integers for now

def rrat():
	return random.randrange(-MAX_INTEGER_MAGNITUDE, MAX_INTEGER_MAGNITUDE)

def euclidean_norm_squared(v):
	return v.dot(v) # Already gives the squared value

def s():
	# Solve the problem...
	a = Matrix([[1],[1],[1]])
	b = Matrix([[1],[-2],[1]])
	I = Matrix([[1,0,0],[0,1,0],[0,0,1]]) # 3x3 identity
	c = Matrix([[rrat()], [rrat()], [rrat()]])
	# Calculate P
	P = (a * a.T) / (euclidean_norm_squared(a)) + (b * b.T) / (euclidean_norm_squared(b))
	while True: # Main bruteforce loop
		lhs = I - P
		c = Matrix([[rrat()], [rrat()], [rrat()]])
		rhs = (c * c.T) / (euclidean_norm_squared(c))
		if simplify(lhs - rhs) == Matrix.zeros(3, 3):
			break
	print("Solution: "+str(c))
	return

if __name__=="__main__":
	s()
	exit(0)
