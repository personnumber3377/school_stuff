
from sympy import *
from math import pi

def s():
	# Solve the shit...
	sigma0, R, Q = symbols("sigma0 R, Q")
	R = 0.248 # in meters
	sigma0 = 6.44*10**(-6)
	Q = 0.56*10**(-6) # in microcoulombs
	Aalku = 4*pi*R**2
	Qalku = sigma0 * Aalku
	Qulkopinta = Qalku - Q
	sigmauusi = Qulkopinta/Aalku
	print(sigmauusi)
	eps0 = 8.854187818*10**(-12) # 8.8541878188(14)×10−12
	print("Qulkopinta: "+str(Qulkopinta))
	E = Qulkopinta / (4*pi*eps0*R**2)
	print("E: "+str(E))
	return

if __name__=="__main__":
	s()
	exit(0)
