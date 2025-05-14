import math

# Constants
C = 150 * 10**6  # Spring constant in J/m² (converted from J/nm²)
m_electron = 9.1093837 * 10**(-31)  # Mass of the electron in kg
h_bar = 1.0545718 * 10**(-34)  # Reduced Planck's constant in J·s

# Debugging the values:
print(f"Spring constant C: {C} J/m²")
print(f"Electron mass m: {m_electron} kg")
print(f"Reduced Planck's constant h_bar: {h_bar} J·s")

# Angular frequency (ω)
w = math.sqrt(C / m_electron)

# Debugging angular frequency
print(f"Angular frequency ω: {w} rad/s")

# Ground state energy (E_0)
E_0 = 0.5 * h_bar * w

# Debugging ground state energy
print(f"Ground state energy E_0 in Joules: {E_0} J")

# Convert energy to eV
eV = 1.60217663 * 10**(-19)  # eV in Joules
E_0_eV = E_0 / eV

# Output results
print(f"Ground state energy in eV: {E_0_eV} eV")
