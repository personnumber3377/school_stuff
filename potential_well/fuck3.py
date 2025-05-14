import math

# Constants
C = 150 * 10**6  # Convert from J/nm² to J/m²
m_electron = 9.1093837 * 10**(-31)  # Electron mass in kg
h_bar = 1.0545718 * 10**(-34)  # Reduced Planck's constant in J·s

# Angular frequency (ω)
w = math.sqrt(C / m_electron)

# Ground state energy (E_0)
E_0 = 0.5 * h_bar * w

# Convert energy to eV
eV = 1.60217663 * 10**(-19)  # eV in Joules
E_0_eV = E_0 / eV

# Output results
print(f"Ground state energy in Joules: {E_0} J")
print(f"Ground state energy in eV: {E_0_eV} eV")
