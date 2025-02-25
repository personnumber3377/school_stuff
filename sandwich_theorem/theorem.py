
from sympy import *
import random
# from sympy import symbols, Abs, sin, forall, Implies, S
'''

In order to use the sandwich theorem, we need to find a function g
 such that |f(u,y)|≤g(u,y)
 and lim(u,y)→(0,0)g(u,y)=0
, to show that lim(u,y)→(0,0)f(u,y)=0
. Among the following choices,
(a) y2

(b) 3|y|

(c) y

(d) 2|u||y|y2+u2

pick the most suitable one for function g
 if we want to show that
lim(u,y)→(0,0)
sin**2(u)(cos(1/y)+cos(1/u))sin(y)/(3y**2+2u**2)=0.


solution_y = solveset(inequality, y, domain=S.Reals)
    
    # Step 2: Solve for u in terms of y
    solution_u = solveset(inequality, u, domain=S.Reals)
    
    # Check if both solutions are non-empty, indicating the inequality holds
    if solution_y != S.EmptySet and solution_u != S.EmptySet:
        satisfied_candidates.append(g)

'''



'''
def iterate_functions(f, gs, symbols): # This function iterates over functions in gs and checks if any of them fulfills the condition abs(f(u,y)) <= g(u,y)
	sols = []
	for g in gs:
		# Now check the thing.
		# s = solve_rational_inequalities([[((abs(f), g), "<=")]]) # Doesn't work for functions, because only applicable to polynomials...
		# s = solve_univariate_inequality
		inequality = abs(f) <= g
		if forall(tuple(symbols), Implies(True, inequality)):
			sols.append(g)
	print("Solutions: "+str(sols))
	return
'''

MAX_INPUT_INT = 0.00001
MIN_INPUT_INT = -MAX_INPUT_INT

INPUT_COUNT = 100

def iterate_functions(f, gs, symbols): # This function iterates over functions in gs and checks if any of them fulfills the condition abs(f(u,y)) <= g(u,y)
	sols = []
	for g in gs:
		#inequality = abs(f) == g
		#solution = solve(inequality, [symbols[0], symbols[1]])
		#sols.append(solution)
		# Just loop over the shit
		# Now just do the shit here...
		issol = True # Assume solution until otherwise.
		for i in range(INPUT_COUNT):
			if i % 100 == 0:
				print(i)
			# u_val = random.randrange(MIN_INPUT_INT, MAX_INPUT_INT)
			#print("U: "+str(u_val))
			#for _ in range(INPUT_COUNT):
			# y_val = random.randrange(MIN_INPUT_INT, MAX_INPUT_INT)
			u_val = random.random()*(MAX_INPUT_INT - MIN_INPUT_INT)+MIN_INPUT_INT
			y_val = random.random()*(MAX_INPUT_INT - MIN_INPUT_INT)+MIN_INPUT_INT
			print("Y: "+str(y_val))
			print("U: "+str(u_val))
			# Now try to solve the thing...
			# Check for nan
			res1 = (abs(f)).subs(symbols[0], u_val).subs(symbols[1], y_val)

			if res1 == nan:
				continue
			res2 = g.subs(symbols[0], u_val).subs(symbols[1], y_val)
			if res2 == nan:
				continue
			if not res1 <= res2:
				issol = False
				# sols.append(g)
		if issol:
			print("Solution: "+str(g))
			sols.append(g)
			#exit(0)

	u = symbols[0]
	y = symbols[1]

	for sol in sols:
		print("Checking "+str(sol))
		if limit(Abs(f) / sol, (u, 0), (y, 0)) == 0:
			print(f"Candidate {g} works!")


	print("Solution: "+str(sols))
	return


def run():
	# The function is this:
	u, y = Symbol("u"), Symbol("y")
	# Now define the function
	f = (sin(u)**2*(cos(1/y)+cos(1/u))*sin(y))/(3*y**2+2*u**2)

	g_functions = [y**2, 3*abs(y), y, 2*abs(u)*abs(y)/(y**2+u**2)]

	# Now loop over the functions and check the thing...

	iterate_functions(f, g_functions, [u,y])

	return


if __name__=="__main__":
	run()
	exit(0)


