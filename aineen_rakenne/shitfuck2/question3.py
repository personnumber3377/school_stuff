
from sympy import * # Import math library

def s():
	# Solve problem
	spin = 1/2 # spin of silver atom
	speed = 890 # m/s
	l_B = 5.7*10**(-2) # 5.7 cm
	dB_dl = 2.5 * 10**3 # The rate of change of the magnetic field.

	m_Ag = 1.7911901*10**(-25) # Mass of the silver atom...

	# We know that F_y = mu_z * db_dl
	# We also know that mu_z = +- 1/2*g_s*mu_B
	# Where mu_B is the bohr magneton and g_s is the spin g-factor (in this case 2)
	g_s = 2
	mu_B = 9.274*10**(-24) # bohr magneton in joules per tesla

	mu_z = 1/2*g_s*mu_B

	# Now we calculate the force on the thing...

	F_y = mu_z * dB_dl # Calculate the force

	# Calculate how much time we spend in the thing...

	t = l_B / speed # How much time we spend in the magnetic field????

	# Now we know that F = m*a therefore a = F / m

	a = F_y / m_Ag

	# Now we just calculate 1/2*a*t**2 to get the thing.

	dY = 1/2*a*t**2

	# Now multiply by two because we were asked for the difference of the two beams

	ans = dY * 2

	print("Answer: "+str(ans))

	return

if __name__=="__main__":
	s()
	exit(0)
