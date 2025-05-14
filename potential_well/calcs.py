
from sympy import *

import math

def s():
	# Solve the thing...
	h = 6.62607015*10**(-34)
	n = 1.0
	m = 9.1093837*10**(-31) # Mass of electron
	L = 0.24*10**(-9) # 0.24 nm
	E = (n**2*h**2)/(8*m*L**2)
	# 1.60217663 × 10-19
	eV = 1.60217663*10**(-19)
	print(E / eV)
	return

def s2():
	# def s():
	# Solve the thing...
	h = 6.62607015*10**(-34)
	n = 1.0
	# m = 9.1093837*10**(-31) # Mass of electron
	m = 10**(-14)
	# L = 0.24*10**(-9) # 0.24 nm
	L = 0.3 * 10**(-3) # 0.3mm

	E = (n**2*h**2)/(8*m*L**2)
	print("Energy: "+str(E))
	v = math.sqrt(2*E/m)
	print("speed: "+str(v))
	F = 2*m*v**2/L
	print("Force: "+str(F))
	freq = v/L
	print(freq)

	# Stuff here...

	C = 150 * 10**(6)

	m_electron = 9.1093837*10**(-31)
	m = m_electron

	w = math.sqrt(C/m)
	
	# h_bar = h / (2*math.pi)
	h_bar = 1.0545718*10**(-34)
	
	# E_0 = 1/2*h_bar*w

	E_0 = h_bar**2*C/(2*m_electron)

	eV = 1.60217663*10**(-19)

	print(E_0)
	print("As electron volts: "+str(E_0 / eV))
	return


if __name__=="__main__":
	s()
	s2()
	exit(0)
