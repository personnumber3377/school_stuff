
from sympy import *

# This function basically gives the answer to this: "b) Mitkä ovat energiat kaikille mahdollisille fotoneille, jotka tämä atomi pystyy emittoimaan, kun atomi on aluksi perustilassaan? (Pienimmästä suurimpaan.)"

def gen_energy_for_photons(energy_levels: list, base_energy) -> list:
	print("We got these energy levels here: "+str(energy_levels))
	energy_levels.append(base_energy)
	energy_levels = sorted(energy_levels, reverse=True)
	print("sorted: "+str(energy_levels))
	o = []
	while len(energy_levels) > 1:
		cur_energy_level = energy_levels.pop(0)

		for other_level in energy_levels:
			o.append(cur_energy_level - other_level)


	return sorted(o)



def s():
	# Now do the thing...
	# 2.1 eV, 4.1 eV ja  4.9 eV
	# eV = 1.60217663*10**(-19) # electron volt to joules
	eV = 1.0
	E0 = -10.6*eV  # e.g., ground state of material in eV
	excited_states = [-2.1*eV, -4.1*eV, -4.9*eV] # excitation energies in eV

	energy_levels = [E0 + dE for dE in excited_states] # The energy levels

	print(energy_levels)

	res = gen_energy_for_photons(energy_levels, E0)
	print(res)


	return

if __name__=="__main__":
	s()
	exit()
