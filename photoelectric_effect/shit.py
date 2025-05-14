
import math

def poopoo():
	# Now do the shit...
	l = 0.1*(10**(-9)) # 0.1 nanometers...
	h = 6.62607015*10**(-34) # 6.62607015×10−34
	m_e = 9.1093837*10**(-31)
	# Because l = h / p = h / (mv) , therefore v = h / (lm)
	v = h / (l*m_e)
	e_k = 1 / 2 * m_e * (v**2) # Kinetic energy.
	# print(e_k)
	eV = 1.60217663*10**(-19)
	electron_volts = e_k / eV
	print(electron_volts)
	# E = h*f
	f = c / l
	E_photon = h*f
	print("poopoooo")
	print(E_photon / eV)
	return

def to_rad(degrees):
	return (2*math.pi)/(360)*degrees

def poopoo2():
	# n*l = 2*d*sin(theta)
	# l = h / p
	# E = p**2 / (2*m_e) => p = sqrt(E*2*m_e)


	m_e = 9.1093837*10**(-31)
	eV = 1.60217663*10**(-19)
	E_k =  72.5*eV
	h = 6.62607015*10**(-34) # 6.62607015×10−34
	p = math.sqrt(E_k*2*m_e)
	l = h / p
	print("l: "+str(l))
	print("p: "+str(p))
	theta = 25.8
	d = l / (2*math.sin(to_rad(theta)))
	print("d: "+str(d))
	return

if __name__=="__main__":
	# E=4.35 eV.
	# E = hf
	E = 4.35 * (1.60217663*(10**(-19))) # 1.60217663 × 10-19 joules
	h = 6.62607015*10**(-34)
	# freq = E / h 
	c = 299792458
	thing = (h*c) / E
	freq = E / h
	print("Freq: "+str(freq))
	momentum = h / thing
	print("Momentum: "+str(momentum))
	print(thing)

	print("Now doing poopoo")
	poopoo()
	poopoo2()
	exit(0)
