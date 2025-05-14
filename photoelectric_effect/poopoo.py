
import numpy as np
import matplotlib.pyplot as plt

def s():
	# Solution

	# Example data: frequency (Hz) and stopping voltage (V)
	# frequencies = np.array([5.0e14, 5.5e14, 6.0e14, 6.5e14])  # Hz
	freqs = [6.84,
		7.92,
		8.94,
		10.1,
		11.0,
		12.1]
	frequencies = np.array([x*10**(14) for x in freqs]) # 10**(14)

	energies = [0.53,
		0.99,
		1.43,
		1.87,
		2.33,
		2.79]

	eV = 1.60217663*10**(-19) # 1.60217663 × 10-19 joules

	energies = np.array([x*eV for x in energies])

	# Linear fit: E = h*f - φ
	coeffs = np.polyfit(frequencies, energies, 1)
	slope, intercept = coeffs
	h_estimate = slope
	phi_estimate = -intercept

	print(f"Estimated Planck's constant h ≈ {h_estimate:.3e} J·s")
	print(f"Estimated work function φ ≈ {phi_estimate:.3e} J")

	# Optional: Plot
	plt.plot(frequencies, energies, 'o', label='Data')
	plt.plot(frequencies, np.polyval(coeffs, frequencies), label='Fit')
	plt.xlabel('Frequency (Hz)')
	plt.ylabel('Kinetic Energy (J)')
	plt.title('Photoelectric Effect (Kinetic Energy vs Frequency)')
	plt.grid(True)
	plt.legend()
	plt.show()

if __name__=="__main__":
	s()
	exit(0)
