



from sympy import *

if __name__=="__main__":
	# u,v,w,z = Symbol("u"), Symbol("v"), Symbol("w"), Symbol("z")
	# These are the equations ( = 0)
	# Define symbols and functions
	#z = symbols('z')
	#w = Function('w')(z)
	#v = Function('v')(z)
	#u = symbols('u')  # u is constant
	w = Symbol('w')
	u = symbols('u')  # u is constant
	# Equations

	z = Function('z')(w, u)
	# w = Function('w')(z)
	
	v = Function('v')(w, u)
	
	dz_dw = symbols('dz_dw')  # Introducing symbolic derivatives
	dv_du = symbols('dv_du')
	dw_du = symbols('dw_du')
	dv_dw = symbols('dv_dw')
	# Define the equations
	eq1 = Eq(2*z + 2*w + v + 3*u*5*z + w + 2*v + u, -4)
	eq2 = Eq(5*z + w + 2*v + u, -2)

	# Differentiate the equations with respect to z
	#diff_eq1 = 15 * u + 3 * dv_dz + 3 * dw_dz + 2  # From initial differentiated form
	#diff_eq2 = 2 * dv_dz + dw_dz + 5


	diff_eq1 = diff(eq1.lhs, w) - diff(eq1.rhs, w)
	diff_eq2 = diff(eq2.lhs, w) - diff(eq2.rhs, w)

	# Simplify the results
	diff_eq1 = simplify(diff_eq1)
	diff_eq2 = simplify(diff_eq2)
	diff_eq1 = Eq(diff_eq1, 0)
	diff_eq2 = Eq(diff_eq2, 0)
	print("diff_eq1 == "+str(diff_eq1))
	print("diff_eq2 == "+str(diff_eq2))

	# Substitute placeholders dz_dw and dv_dw
	diff_eq1 = diff_eq1.subs(Derivative(z,w), dz_dw)
	diff_eq2 = diff_eq2.subs(Derivative(z,w), dz_dw)
	# Substitute dw_du
	diff_eq1 = diff_eq1.subs(Derivative(v,w), dv_dw)
	diff_eq2 = diff_eq2.subs(Derivative(v,w), dv_dw)

	#print(diff_eq1)
	#print(diff_eq2)

	res = solve([diff_eq1, diff_eq2], [dz_dw, dv_dw])
	print("Here is the bullshit:")
	# print(res.subs(u, 2))
	print(res)


	w = Symbol('w')
	u = symbols('u')  # u is constant
	# Equations
	z = Symbol('z')
	#z = Function('z')(u, w)
	# w = Function('w')(z)
	
	v = Function('v')(u, w)



	#w = Symbol('w')
	#u = symbols('u')  # u is constant
	# Equations

	#z = Function('z')(w, u)
	# w = Function('w')(z)
	
	#v = Function('v')(w, u)
	


	

	dz_dw = symbols('dz_dw')  # Introducing symbolic derivatives
	dv_du = symbols('dv_du')
	dw_du = symbols('dw_du')
	dv_dw = symbols('dv_dw')
	dz_du = symbols('dz_du')
	# Define the equations
	eq1 = Eq(2*z + 2*w + v + 3*u*5*z + w + 2*v + u, -4)
	eq2 = Eq(5*z + w + 2*v + u, -2)


	diff_eq1 = diff(eq1.lhs, u) - diff(eq1.rhs, u)
	diff_eq2 = diff(eq2.lhs, u) - diff(eq2.rhs, u)

	# Simplify the results
	diff_eq1 = simplify(diff_eq1)
	diff_eq2 = simplify(diff_eq2)
	diff_eq1 = Eq(diff_eq1, 0)
	diff_eq2 = Eq(diff_eq2, 0)
	print("diff_eq1 == "+str(diff_eq1))
	print("diff_eq2 == "+str(diff_eq2))


	diff_eq1 = diff_eq1.subs(Derivative(v,u), dv_du)
	diff_eq2 = diff_eq2.subs(Derivative(v,u), dv_du)
	# Substitute dw_du
	diff_eq1 = diff_eq1.subs(Derivative(z,u), dz_du)
	diff_eq2 = diff_eq2.subs(Derivative(z,u), dz_du)

	print(diff_eq1)
	print(diff_eq2)

	res = solve([diff_eq1, diff_eq2], [dv_du, dz_du])
	# print(res.subs(u, 2))
	print("Here is the other bullshit:")
	print(res)
	# print(res.subs(u, 3).subs(w, 2))
	# Solve for dw/dz
	# explicit_solution = solve([diff_eq1, diff_eq2], (Derivative(z, w)))
	# print(explicit_solution)
	exit(0)





'''
I was given the following prompt: ```Quantities u, v, w and z satisfy the equations 2*z+2*w+v+3*u=-4 and 5*z+w+2*v+u=-2  find the partial derivatives (dz/dw)_u and (dv/du)_w at (3,2).``` I was also given the hint: Remember: (dz/dw)_u equals (dz(w,u)/dw) that is z is a function of w and u but it is not a function of v which is a function of w and u. I do not understand how the hint makes sense, since the subscript means that the quantity u remains constant, so therefore how can z be a function of w and u , when u is a constan? Please explain

'''




















