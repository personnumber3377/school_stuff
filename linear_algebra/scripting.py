import numpy as np
from fractions import Fraction

# Define inner product as in (1)
def inner_product(x, y):
    return x[0]*y[0] + 2*x[1]*y[1] + 3*x[2]*y[2]

def calc_coeff(target_vector, basis): # Calculates coefficients
    # Calculate coefficients
    coeffs = []
    for u in basis:
        # I think that this here should be memoized
        c = inner_product(target_vector, u) / inner_product(u, u) # Inefficient, since we could memoize the inner_product of the basis vectors, but I don't care.
        coeffs.append(c)
    return coeffs

def to_frac(list_of_numbers):
    fractions = [Fraction(d).limit_denominator() for d in list_of_numbers]
    return fractions

if __name__=="__main__":

    # 3. Let q1 = [0, 3, 2]T , q2 = [15, 3, −3]Tand q3 = [−1, 1, −1]T
    # Orthogonal basis vectors (not necessarily normalized)
    u1 = np.array([0, 3, 2])
    u2 = np.array([15, 3, -3])
    u3 = np.array([-1, 1, -1])

    # Target vector to express as a linear combination
    v = np.array([1, 2, 3])
    w = np.array([4, -2, 1])

    # Put the orthogonal vectors into a list
    basis = [u1, u2, u3]

    v_coeffs = calc_coeff(v, basis)
    w_coeffs = calc_coeff(w, basis)

    # Convert to fractions:
    v_coeffs = to_frac(v_coeffs)
    w_coeffs = to_frac(w_coeffs)

    print("Coefficients for v:", v_coeffs)
    print("Coefficients for w:", w_coeffs)

