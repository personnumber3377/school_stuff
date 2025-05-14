
from sympy import *

def s():
	# Solution here...
	eps, delta = symbols("eps delta")
	mat = Matrix([[1+eps**2, 1], [1, 1+eps**2]])
	eig_vals = mat.eigenvals()
	print(eig_vals)
	mat_inv = mat**-1
	print(mat_inv)
	b_vec = Matrix([[2],[2-delta]])
	# Apply inverse matrix here.
	res = mat_inv @ b_vec
	print(res)
	# Now let's try to substitute epsilon approaches zero and delta is zero
	print("As epsilon approaches zero and delta is zero: "+str(res.subs(delta, 0).subs(eps, 0.00001)))
	print("As epsilon approaches zero and delta is not zero: "+str(res.subs(eps, 0.0000001)))
	return

if __name__=="__main__":
	s()
	exit(0)
