import math

def poopoo2():
    # Constants
    m_e = 9.1093837 * 10**(-31)  # Electron mass in kg
    eV = 1.60217663 * 10**(-19)  # Conversion factor from eV to Joules
    h = 6.62607015 * 10**(-34)  # Planck's constant in J·s
    
    # Kinetic energy of the electron (in Joules)
    E_k = 72.5 * eV
    
    # Calculate momentum p = sqrt(2 * E_k * m_e)
    p = math.sqrt(2 * E_k * m_e)
    
    # Calculate the de Broglie wavelength l = h / p
    l = h / p
    
    # Print the de Broglie wavelength and momentum
    print("l (wavelength): " + str(l))
    print("p (momentum): " + str(p))
    
    # Diffraction angle in degrees
    theta = 25.8
    
    # Apply Bragg's law: d = l / (2 * sin(theta))
    d = l / (2 * math.sin(math.radians(theta)))
    
    # Print the interplanar distance
    print("d (interplanar distance): " + str(d))
    
    return

# Call the function
poopoo2()
