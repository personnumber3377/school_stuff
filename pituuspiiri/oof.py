
from math import *

def to_rad(degrees):
	return (2*pi)/360*degrees

def s():
	# Solution here.
	phi1 = to_rad(30)
	phi2 = to_rad(30)
	delta_lambda = to_rad(90)
	res = acos(sin(phi1)*sin(phi2)+cos(phi2)*cos(phi1)*cos(delta_lambda))
	print(res)
	print(res*6371)
	return

if __name__=="__main__":
	s()
	exit(0)
