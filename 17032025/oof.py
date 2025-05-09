
from sympy import *
# from math import *

def s():
	u,v = symbols("u v")
	x = (1+v/2*cos(u/2))*cos(u)
	y = (1+v/2*cos(u/2))*sin(u)
	z = v/2*sin(u/2)

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

	print("Here is the stuff for r_v: "+str(", ".join(str(k) for k in r_v)))


	substituted_r_u_1 = [thing.subs("u", 0).subs("v", 0) for thing in r_u]
	print(substituted_r_u_1)
	substituted_r_v_1 = [thing.subs("u", 0).subs("v", 0) for thing in r_v]
	print(substituted_r_v_1)

	# And then when two pi

	substituted_r_u_2 = [thing.subs("u", 2*pi).subs("v", 0) for thing in r_u]
	print(substituted_r_u_2)
	substituted_r_v_2 = [thing.subs("u", 2*pi).subs("v", 0) for thing in r_v]
	print(substituted_r_v_2)

	print("Now the point stuff...")

	point1 = [thing.subs("u", 0).subs("v", 0) for thing in r]
	point2 = [thing.subs("u", 2*pi).subs("v", 0) for thing in r]

	print("Point1: "+str(point1))
	print("Point2: "+str(point2))
	

	return

if __name__=="__main__":
	s()
	exit()

