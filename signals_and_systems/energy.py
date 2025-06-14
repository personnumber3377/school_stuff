
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
	E1 = simplify(integrate(x1**2, (t, -oo, oo)))
	E2 = simplify(integrate(x2**2, (t, -oo, oo)))

	print(f"Energy of x1(t): {E1}")
	print(f"Energy of x2(t): {E2}")

	return


if __name__=="__main__":
	s()
	exit()
