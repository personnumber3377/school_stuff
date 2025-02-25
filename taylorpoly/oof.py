
from sympy import *

def taylor_polynomial(f, x, y, a, b, order=2):
    # First-order partial derivatives
    fx = diff(f, x)
    fy = diff(f, y)

    # Second-order partial derivatives
    fxx = diff(fx, x)
    fyy = diff(fy, y)
    fxy = diff(fx, y)

    # Evaluate derivatives at (a, b)
    f_0 = f.subs({x: a, y: b})
    fx_0 = fx.subs({x: a, y: b})
    fy_0 = fy.subs({x: a, y: b})
    fxx_0 = fxx.subs({x: a, y: b})
    fyy_0 = fyy.subs({x: a, y: b})
    fxy_0 = fxy.subs({x: a, y: b})

    # Construct Taylor polynomial
    taylor_poly = (
        f_0
        + fx_0 * (x - a)
        + fy_0 * (y - b)
        + (1 / 2) * fxx_0 * (x - a)**2
        + (1 / 2) * fyy_0 * (y - b)**2
        + fxy_0 * (x - a) * (y - b)
    )

    return taylor_poly.simplify()

if __name__=="__main__":
    x, y = Symbol("x"), Symbol("y") # Our variables...
    variables = [x, y]
    f = x*E**(-y)  # y*E**(x*y**2) # x*E**(-x*y**2)
    poly = taylor_polynomial(f, x, y, -2, -1, order=2)
    print(poly)
    
    exit(0)


# E*(-1.5*x**2 + 6.0*x*y - 7.0*x - 3.0*y**2 + 10.0*y - 7.5)
# E*(-1.5*x**2 + 6.0*x*y - 7.0*x - 3.0*y**2 + 10.0*y - 7.5)

# e*(-3/2*x**2 + 6*x*y - 7*x - 3*y**2 + 10*y - 15/2)
# e*(1/2*x**2 - 5*x*y + 5*x + 5*y**2 - 12*y + 15/2)

# 1*(-16*x**2 + 20*x*y + 80*x - 10*y**2 - 67*y - 120)*e**(-4)
# (-16*x**2 + 44*x*y + 112*x - 22*y**2 - 123*y - 168)*e**(4)

# e*(-1*x*y - 1*y**2 - 2*y - 1)
