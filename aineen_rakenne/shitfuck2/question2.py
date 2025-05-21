
# This script essentially answers the question: Vetyatomin perustilan normoitu aaltofunktio on ψ1s(r)=1πa30√e−r/a0, missä a0 on Bohrin säde.

from sympy import *

def s():
	# solve the thing...
	r = symbols("r")
	
	a0 = 5.29177210903*10**(-11)  # Borhs radius

	# Now define the wave function

	phi_s1 = 1/(sqrt(pi*a0**3))*E**(-r/a0)

	# Now do the bullshit maybe???

	# Now since the integral is radial, we only need to do this kinda shit here...

	result = integrate(abs(phi_s1)**2*4*pi*r**2, (r, 0, a0)) # Integrate to the borhs radius????????

	print("Here is the result of the integral: "+str(result))



	# b) Laske etäisyys, jolla esiintymistodennäköisyystiheydellä on suurin arvo. (Anna vastaus Bohrin säteen yksiköissä 'a0').

	# Basically just take the derivative and then try to find the minimum of that maybe????????

	# diff_thing = diff(phi_s1, r)
	# We need to use this thing: Abs(phi_s1)**2 * r**2

	diff_thing = diff(phi_s1**2 * r**2, r) # diff(Abs(phi_s1)**2 * r**2, r)

	print("diff_thing: "+str(diff_thing))
	stuff = Eq(diff_thing, 0) # Set derivative to zero

	sol = solve(stuff, r)
	print(sol)
	actual_sol = sol[1] # Pick out the actual solution for now...

	print("As a0: "+str(actual_sol/a0))

	# c) Laske elektronin etäisyyden r odotusarvo. (Anna vastaus Bohrin säteen yksiköissä 'a0').

	# Basically the same as a, except integrate over all space and multiply the integral shit by r:

	result = integrate(r*abs(phi_s1)**2*4*pi*r**2, (r, 0, oo)) # oo is infinity in sympy

	print("Here is the expected position maybe: "+str(result / a0)+" as a0.")

	return

from math import pi

def s2():
	# Do the stuff here maybe...

	eV = 1.60217663*10**(-19)
	a0 = 5.29177210903*10**(-11)
	eps0 = 8.854187817*10**(-12)

	q = 1.60217663*10**(-19)

	electrostatic_potential = - 1 / (4*pi*eps0) * q**2 / (a0)

	kinetic_energy = 1 / 2 * q**2 / (4*pi*eps0*a0)

	print("Electrostatic potential energy: "+str(electrostatic_potential / eV))

	print("Kinetic energy: "+str(kinetic_energy / eV))

	return 


def question4():
	# Do the shit here maybe????

	B = 1.8 # 1.8 tesla magnetic field...

	# dE = mu_B * B * m_l

	mu_B = 5.788*10**(-5) # electron volts

	dE = mu_B * B

	print("Difference in energy in electron volts: "+str(dE))

	# c) Mikä on tässä transitiossa emittoituvan fotonin aallonpituus, kun Δmℓ=0?

	# So we can just calculate this using the dE = h*c/lambda and therefore  lambda = h*c/dE . In addition we can just use the R*(1/n1**2 - 1/n2**2) formula for the energy difference.
	n1 = 3
	n2 = 2
	R = -13.6# *(1/)
	dE = R*(1/n1**2 - 1/n2**2) # Calculate the shit.

	# Convert to joules first
	# eV = 
	eV = 1.60217663*10**(-19)
	dE = dE*eV

	# Now calculate the thing.
	c = 299792458
	h = 6.62607015*10**(-34)
	lambda_val = h*c/dE

	print("Value for the wavelength: "+str(lambda_val))

	# Energy difference initial

	energy_initial = dE

	# Now try to calculate the effect the dE = mu_B * B * m_l # Do the shit here...
	mu_B_eV = mu_B * eV
	dE_new = mu_B_eV * B * 1 # The difference in the thing is 1

	assert dE_new <= energy_initial

	new_energy_diff = energy_initial - dE_new
	actual_energy = energy_initial
	# Now do the stuff...

	lambda_val_new = h*c/new_energy_diff
	diff = lambda_val - lambda_val_new
	print("Differnece thing: "+str(diff))

	return

def calc_mu(m1, m2):
	return (m1*m2) / (m1 + m2)

def question6():
	# Do the thing here maybe???
	l1 = 3
	l2 = 4
	h_bar = 1.054571817*10**(-34)
	difference = (l2*(l2 + 1) - l1*(l1 + 1))
	r = 189*10**(-12) # picometers
	sulphur_atom_mass_au = 32.065 # 5.3245181*10**-(26)
	mu = calc_mu(sulphur_atom_mass_au, sulphur_atom_mass_au)
	mu = mu * (1.66053873*10**(-27))
	dE = h_bar**2 / (2*mu*r**2)*difference 
	eV = 1.60217663*10**(-19)
	print("Energy difference: "+str(dE / eV))
	return

if __name__=="__main__":
	s()
	s2()
	question4()
	question6()
	exit(0)
