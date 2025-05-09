
from sympy import *
# from math import *


def jacobian(f, x): # Computes the jacobian of list of functions in f with respect to variables in list x.
	res = []
	for function in f:
		to_append = []
		for var in x:
			to_append.append(diff(function, var))
		res.append(to_append)
	return res


def get_cross(v1,v2):
	assert len(v1) == 3 and len(v1) == len(v2)
	a,b,c = v1
	d,e,f = v2
	return [(b*f - c*e), (c*d - a*f), (a*e - b*d)]

def s():
	# r(u, v) = ((R + r cos v) cos u,(R + r cos v) sin u, r sin v),

	r, R, u, v = symbols("r R u v") # Just define some stuff...

	param = [(R+r*cos(v))*cos(u), (R+r*cos(v))*sin(u), r*sin(v)]

	x,y,z = param[0], param[1], param[2]

	x_u = diff(x,u)
	y_u = diff(y,u)
	z_u = diff(z,u)

	r = [x,y,z]

	r_u = [x_u, y_u, z_u]
	print("Here is the stuff for r_u: "+str(", ".join(str(k) for k in r_u)))

	x_v = diff(x,v)
	y_v = diff(y,v)
	z_v = diff(z,v)

	r_v = [x_v, y_v, z_v]

	cross = get_cross(r_u, r_v)

	print("Cross product: "+str(cross))

	x1,x2,x3 = cross

	# Now compute magnitude

	mag = sqrt(x1**2+x2**2+x3**2)
	print(mag)
	mag = simplify(mag)
	mag = simplify(mag)
	print("Magnitude is this: "+str(mag))

	# Now do the shit maybe???

	# j = jacobian(param, [u,v])

	# print("Jacobian is this here: "+str(j))

	# sqrt(k**2*cos(u)**2*cos(v)**2+k**2*sin(u)**2*cos(u)**2+k**2*sin(u)**4*sin(v)**2+2*k**2*sin(u)**2*sin(v)**2*cos(u)**2+k**2*sin(v)**2*cos(u)**4)

	# finally(u,v):=cos(u)**2*cos(v)**2+sin(u)**2*cos(v)**2+sin(u)**4*sin(v)**2+2*sin(u)**2*sin(v)**2*cos(u)**2+sin(v)**2*cos(u)**4

	return

if __name__=="__main__":
	s()
	exit()

