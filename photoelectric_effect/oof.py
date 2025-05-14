
import math

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
	poopoo2()
	exit(0)
