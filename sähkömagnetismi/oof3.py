 
from sympy import *

def s():
    d, l, rho, g, B, I = symbols("d l rho g B I")
    # B = 50*(10**(-6)) # 50 microteslas
    I = 900
    d = 0.005 # 5 mm
    rho = 8900 # kg/m**3
    g = 9.81
    # equation = Eq(I*(l*cos(pi/4)*B), pi*(d/2)**2*l*rho*g)
    equation = Eq(I*(l*B), pi*(d/2)**2*l*rho*g)
    sol = solve(equation, B)
    print("Solution: "+str(sol))
    return


if __name__=="__main__":
    s()
    exit(0)


