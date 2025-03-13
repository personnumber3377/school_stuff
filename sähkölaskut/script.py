
from sympy import *

def sol():
    q = Symbol("q")
    epsilonzero = 8.854*10**(-12)
    k = 1/(4*pi*epsilonzero)
    eq = Eq((10**8)*9.81, k*q**2)
    solution = solve(eq, q)
    print("Solution for q: "+str(solution))
    q_sol = abs(solution[0])
    n_coul = 6.25*(10**18)
    num_of_electrons = q_sol*n_coul
    print("Number of electrons: "+str(num_of_electrons))
    V_Au = 10**(-9)
    d_Au = 19320
    m_Au = V_Au*d_Au
    # Now we have the mass of the gold, convert to moles and then convert to atoms of gold.
    N_avog = 6.022*10**(23)
    molar_mass_of_gold = 0.19697 # kg/mol
    atoms_of_gold = m_Au/molar_mass_of_gold*N_avog
    print("Mass of gold: "+str(m_Au))
    print("Atoms of gold: "+str(atoms_of_gold))
    print(num_of_electrons/atoms_of_gold)
    return

if __name__=="__main__":
    sol()
    exit(0)
