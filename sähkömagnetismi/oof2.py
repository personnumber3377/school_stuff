
from sympy import *
from math import pi

def s():
    d, l, rho, g, B, I = symbols("d l rho g B I")
    # B = 50*(10**(-6)) # 50 microteslas
    l = 0.10 # 10cm in meters
    # I = 900
    B = 1.0 # 1 tesla
    I = 10 
    d = 0.005 # 5 mm
    rho = 8900 # kg/m**3
    g = 9.81
    # equation = Eq(I*(l*cos(pi/4)*B), pi*(d/2)**2*l*rho*g)
    # equation = Eq(I*(l*B), pi*(d/2)**2*l*rho*g)
    # sol = solve(equation, B)

    force = I*l*B - pi*(d/2)**2*l*rho*g
    print("Force: "+str(force))
    mass = force / g
    mass = simplify(mass)
    print("Solution: "+str(mass))
    return


if __name__=="__main__":
    s()
    exit(0)


