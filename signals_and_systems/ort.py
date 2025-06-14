
from sympy import *

def s():
	# Problem 2

	# 1. Symbolic triangular pulse
	τ = symbols('τ', real=True)
	# This is needed to make the piecewise defined function play nicely with sympy
	tria = (1 - Abs(τ)) * Heaviside(1 - Abs(τ))     # 0 outside |τ|≤1

	# 2. Define x1(t) and x2(t)
	t = symbols('t', real=True)
	x1 = 2 * tria.subs(τ, 2*t - 1)       # 2·tria((t-½)/(½))
	x2 = -2 * tria.subs(τ, 2*t + 1)      # -2·tria((t+½)/(½))

	# 3. Energy integrals
	# oo is infinity in sympy
	is_orthogonal = (simplify(integrate(x1*x2, (t, -oo, oo))) == 0) # If the result of the integral of x1(t) * x2(t) is zero, then we know that they are orthogonal.

	print("Orthogonal? : "+str(is_orthogonal))

	# Check orthonormality too.

	return


if __name__=="__main__":
	s()
	exit()
