
from sympy import *
import numpy as np

'''

Opiskelija tutkii laserin valon aallonpituutta diffraktion avulla. Hän valaisee laserilla kapeaa rakoa, jonka leveys D=0.03500 mm
. Hän asettaa varjostimen raon taakse etäisyydelle 1.430 m
 tutkiakseen muodostuvaa diffraktiokuviota. Kuvion tummat juovat esiintyvät varjostimelle taulukon osoittamalla tavalla, kun m
 on minimin kertaluku ja etäisyys on mitattu diffraktiokuvion keskikohdasta.


m
 (-)	m1
m2
m3
m4
m5
m6
m7
m8
etäisyys (m)

0.0221
0.0506
0.0744
0.0907
0.1204
0.1454
0.1767
0.1868

Määritä kulma θ
 jokaiselle kertaluvulle, ja piirrä kuvaaja arvoille sinθ
 järjestysluvun m
 funktiona. Kuvaajan ja parhaan mahdollisen lineaarisen sovituksen perusteella määritä laserin aallonpituus.



'''


def s():
	# Solve the diffraction equation d*sin(theta) = m*lambda
	# Therefore sin(theta) = slope*lambda
	x_values = np.array([0.0221, 0.0506, 0.0744, 0.0907, 0.1204, 0.1454, 0.1767, 0.1868])
	m_values = np.array(range(1, len(x_values)+1))
	print(x_values)
	print(m_values)
	L = 1.430  # Distance from slit to screen in meters
	theta = np.arctan(x_values / L)
	sin_theta = np.sin(theta)

	slope, intercept = np.polyfit(m_values, sin_theta, 1)
	D = 0.03500e-3  # Slit width in meters
	wavelength = slope * D

	print(wavelength)
	print("Wavelength (nm):", wavelength * 1e9)

	# Approximate sin(theta) ≈ x / L (small-angle approximation)
	# sin_theta = 

	return

if __name__=="__main__":
	s()
	exit(0)


