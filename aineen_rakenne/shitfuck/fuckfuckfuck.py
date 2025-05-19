
from math import sqrt, pi

def s():
	# Run the shit..

	# dI/I = -2K*dL where K is kappa and dL is the change in length.
	dL = 0.022*10**(-9) # 0.022 nm
	m_e = 9.1093837*(10**(-31))
	m = m_e

	h = 6.62607015*10**(-34)
	h_bar = h / (2*pi) # Divide by 2*pi

	eV = 1.60217663*10**(-19)

	W0 = 2.28*eV

	K = sqrt(2*m*W0)/h_bar
	
	res = -2*K*dL
	print(res)
	return

if __name__=="__main__":
	s()
	exit()