
from sympy import *

t = symbols('t')

x = Matrix([
    [(t + 1) * exp(2*t)],
    [t * exp(2*t)]
])

x_dot = x.diff(t)  # dx/dt
print("x'(t):")
pprint(x_dot)

A = Matrix([[3, -1], [1, 1]])
Ax = A @ x
print("A * x(t):")
pprint(Ax)

print("Simplified shit here: "+str(simplify(x_dot - Ax)))

assert simplify(x_dot - Ax) == Matrix([[0], [0]])
print("✅ Verified: x'(t) == A * x(t)")



x_0 = x.subs(t, 0)
print("x(0):")
pprint(x_0)



assert x_0 == Matrix([[1], [0]])
print("✅ Verified: x(0) = [1, 0]")