from sympy import *


eps = 10**(-90)
A = Matrix([[1,1],[eps,0],[-eps,0]])

print(A.nullspace())

