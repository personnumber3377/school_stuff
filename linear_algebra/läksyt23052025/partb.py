from sympy import *

def s():
    V = Matrix([[1,1],[2,1],[1,2],[0,1]])
    W = Matrix([[2,1],[1,1],[1,1],[0,1]])

    # Concatenate to form a full-rank basis for R^4
    M = V.row_join(W)

    # Inverse of M
    M_inv = M.inv()

    # Take first 2 rows of M_inv to extract V-components
    P = V @ M_inv[:2, :]

    print("P: "+str(P))
    print("As latex: "+latex(P))

if __name__=="__main__":
    s()
    exit(0)