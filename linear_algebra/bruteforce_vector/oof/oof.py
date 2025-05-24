from sympy import *
import random

def euclidean_norm(vector):
    return (vector.T * vector)[0]

def s():
    a = Matrix([[1],[1],[1]])
    b = Matrix([[1],[-2],[1]])
    I = eye(3)

    # Correct orthogonal vector
    c = a.cross(b).reshape(3, 1)

    # Compute P
    P = (a * a.T) / euclidean_norm(a) + (b * b.T) / euclidean_norm(b)
    lhs = I - P
    rhs = (c * c.T) / euclidean_norm(c)

    print("lhs:")
    pprint(lhs)
    print("\nrhs:")
    pprint(rhs)

    print("\nDifference:")
    pprint(simplify(lhs - rhs))

    print("\nEqual? ", lhs.equals(rhs))

if __name__ == "__main__":
    s()
