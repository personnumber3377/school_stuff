 
from sympy import *
import math
def s():
    d, l, rho, g, B, I = symbols("d l rho g B I")
    # B = 50*(10**(-6)) # 50 microteslas
    N = 50
    I = 0.97
    B = 0.25
    R = 0.013 / 2 # 1.3 cm / 2
    angle = math.radians(60) # 60 degrees
    sol = N*I*2*math.pi*R*B*math.sin(angle)
    
    print("Solution: "+str(sol))
    return


if __name__=="__main__":
    s()
    exit(0)


