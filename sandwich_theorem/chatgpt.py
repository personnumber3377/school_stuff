

from sympy import symbols, Abs, sin, cos, limit

# Define variables and the function
u, y = symbols('u y')
f = (sin(u)**2 * (cos(1/y) + cos(1/u)) * sin(y)) / (3*y**2 + 2*u**2)

# List of candidate functions
g_candidates = [y**2, 3*Abs(y), y, 2*Abs(u)*Abs(y)/(y**2 + u**2)]

# Check each candidate
for g in g_candidates:
    # Check the inequality |f(u, y)| <= g(u, y)
    if limit(g, (u, 0), (y, 0)) == 0:
        print(f"Candidate {g} works!")
