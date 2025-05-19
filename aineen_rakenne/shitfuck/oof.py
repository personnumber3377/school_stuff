
from math import sqrt, pi, e

'''


Hiukkassuihkun energia E=4 eV
 ja se törmää potentiaalivalliin, jonka korkeus U0=5 eV
 ja paksuus ℓ=0.78 nm
. Oletetaan, että hiukkassuihkulla kuljetetaan sähköisesti yhden ampeerin virtaa. Kuinka kauan keskimäärin kokeilijan on odotettava, että ensimmäinen hiukkanen läpäisee kokonaan vallin eli pääsee toiselle puolelle vallin läpi, kun hiukkassuihku muodostuu

a) elektroneista?

Δte≈10
^
 s

b) protoneista?

Δtp≈10
^
 s

Ilmoita vastauksessa vain kymmenpotenssi ilman yksikköä.
'''



h = 6.62607015*10**(-34)
h_bar = h / (2*pi) # Divide by 2*pi

eV = 1.60217663*10**(-19)

m_e = 9.1093837*(10**(-31)) # Mass of electron
m_p = 1.67262192*(10**(-27)) # Mass of proton

E = 4*eV
U0 = 5*eV

l = 0.78 * 10**(-9)

q = 1.60217663*10**(-19) # Electron charge in coulombs

def kappa(m):
	return sqrt(2*m*(U0 - E)) / h_bar

def e_stuff(kappa_val):
	return e**(2*kappa_val*l)

def dT(e_stuff):
	return e_stuff * q

def s():
	# Run the shit..

	# dI/I = -2K*dL where K is kappa and dL is the change in length.
	# dL = 0.022*10**(-9) # 0.022 nm
	# m = m_e


	kappa_electron = kappa(m_e) # Electron
	kappa_proton = kappa(m_p) # Proton

	# Now do the stuff...

	e_stuff_electron = e_stuff(kappa_electron)
	e_stuff_proton = e_stuff(kappa_proton)

	dT_electron = dT(e_stuff_electron)
	dT_proton = dT(e_stuff_proton)

	print("Proton, then electron")
	print(dT_proton)
	print(dT_electron)

	return

if __name__=="__main__":
	s()
	exit()