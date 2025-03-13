

from sympy import *

def force_thing(q1,q2,r,k):
	return k*(q1*q2)/(r**2)

def sol():
	k,q1,Q2,s = symbols("k q1 Q2 s")
	# Now solve.
	r = s/sqrt(2) # The thing
	F_Q = force_thing(q1,Q2,r,k)
	F_s = force_thing(q1,q1,s,k)
	F_2r = force_thing(q1,q1,2*r,k)
	rhs = 2*F_s*cos(pi/4)+F_2r
	lhs = F_Q
	print(rhs)
	equation = Eq(rhs, lhs)
	solution = solve(equation, Q2)
	print("Solution: "+str(solution))
	return

if __name__=="__main__":
	sol()
	exit(0)
